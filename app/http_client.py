import httpx
from httpx import AsyncClient
from loguru import logger


class HttpClient:
    client = None

    @staticmethod
    async def instantiate_client():
        if HttpClient.client:
            logger.info("http client already instantiated")
            return
        HttpClient.client = httpx.AsyncClient()
        logger.info("instantiating http client")

    @staticmethod
    async def get_http_client() -> AsyncClient:
        return HttpClient.client

    @staticmethod
    async def close_http_client():
        logger.info("closing down http client")
        await HttpClient.client.aclose()
