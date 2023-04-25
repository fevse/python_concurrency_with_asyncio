import asyncio
from util import async_timed, delay

@async_timed()
async def main():
    delay_times = [2, 3, 4]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]

asyncio.run(main())

