import asyncio

event = asyncio.Event()

async def writer(queue, delay):
    i = 0
    await asyncio.sleep(delay)
    while not event.is_set():
        await queue.put(f'{i}_{delay}')
        i += 1
        await asyncio.sleep(delay)

async def stacker(queue, stack):
    while not event.is_set():
        el = await queue.get()
        stack.append(el)

async def reader(stack, num, delay):
    await asyncio.sleep(delay)
    for _ in range(num):
        while not stack:
            await asyncio.sleep(0)
        el = stack.pop()
        print(el)
        await asyncio.sleep(delay)
    event.set()

async def main():
    delay1, delay2, delay3, num = eval(input())
    queue = asyncio.Queue()
    stack = []

    await asyncio.gather(
        writer(queue, delay1),
        writer(queue, delay2),
        stacker(queue, stack),
        reader(stack, num, delay3)
    )

asyncio.run(main())
