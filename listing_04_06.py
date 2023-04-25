import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed, fetch_status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(100)]
# асинхронное выполнение (быстрое)
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
# синхронное выполнение (очень долгое)
#        status_codes = [await fetch_status(session, url) for url in urls]
        print(status_codes)

asyncio.run(main())

