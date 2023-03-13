from contextlib import asynccontextmanager
from fastapi import FastAPI
from http_client import HttpClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Instantiate the http client at app startup...
    await HttpClient.instantiate_client()
    yield
    # ....and close it down when the app stops
    await HttpClient.close_http_client()


app = FastAPI(title="testing", lifespan=lifespan)


@app.get("/hello")
async def do_the_stuff():
    # You can get_http_client anywhere in your app to get the httpx client using
    # This allows you to avoid having to instantiate the client everytime you make an http request (using "async with httpx.AsyncClient() as client")
    # which is super expensive if you're making lots of http calls
    client = await HttpClient.get_http_client()
    result = await client.get('https://www.python.org/')
    return {
        'status': result.status_code,
        'httpx_client_id': hex(id(client))
    }


@app.get("/hello2")
async def do_the_stuff():
    client = await HttpClient.get_http_client()
    result = await client.get('https://pypi.org/')
    return {
        'status': result.status_code,
        'httpx_client_id': hex(id(client))
    }

