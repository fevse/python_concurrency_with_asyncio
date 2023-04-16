import asyncio

async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} секунд ...')
    await asyncio.sleep(delay_seconds)
    print(f'... сон в течение {delay_seconds} секунд закончился')
    return delay_seconds

