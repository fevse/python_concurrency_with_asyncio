import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed

async def fetch_status(session: ClientSession, url: str, delay: int=0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://example.com', 1),
                    fetch_status(session, 'https://example.com', 1),
                    fetch_status(session, 'https://example.com', 11)]
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)

asyncio.run(main())
