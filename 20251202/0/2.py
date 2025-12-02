import asyncio

async def late(delay, msg):
    await asyncio.sleep(delay)
    print(msg)
    return delay

async def main():
    res = await asyncio.gather(
            late(3, "A"),
            late(1, "B"),
            late(2, "C"),
    )
    print(res)

asyncio.run(main())
