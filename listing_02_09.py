import asyncio
from util import delay

async def main() -> None:
    sleep_for_five = asyncio.create_task(delay(5))
    sleep_again = asyncio.create_task(delay(4))
    sleep_once_more = asyncio.create_task(delay(3))

    await sleep_for_five
    await sleep_again
    await sleep_once_more

asyncio.run(main())

