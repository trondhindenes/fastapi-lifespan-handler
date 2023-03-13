# fastapi-lifespan-handler

If your FastAPI app makes a lot of outgoing http calls, 
you might have seen that httpx' documented async way of doing this is really slow: 

```
async with httpx.AsyncClient() as client:
    client.get("https://stuff")
```

FastApi now has a application-level context manager, 
which is the perfect place to instantiate a global http client which you can 
reuse whenever your app needs to make a http request.

This will cause much higher performance and lower cpu usage.



