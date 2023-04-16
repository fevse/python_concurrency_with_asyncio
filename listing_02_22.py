import asyncio
from util import delay

def call_later():
    print('Меня скоро вызовут')

async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)

asyncio.run(main())
