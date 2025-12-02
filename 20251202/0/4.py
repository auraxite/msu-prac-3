import asyncio

async def squarer(n):
    return n ** 2

async def doubler(n):
    return n * 2

async def main(lst):
    t1 = await asyncio.gather(*[squarer(i) for i in lst])
    t2 = await asyncio.gather(*[doubler(i) for i in t1])
    print(t2)

asyncio.run(main(range(10)))

