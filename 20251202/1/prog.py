import asyncio

async def writer(queue, delay, event):
    i = 0
    while True:
        await asyncio.sleep(delay)
        if event.is_set():
            break
        await queue.put(f'{i}_{delay}')
        i += 1

async def stacker(queue, stack, event):
    while True:
        await asyncio.sleep(0)
        if event.is_set():
            break
        try:
            stack.append(queue.get_nowait())
        except Exception:
            continue

async def reader(stack, j, delay, event):
    await asyncio.sleep(delay)
    while j:
        if not stack:
            await asyncio.sleep(0.1)
            continue
        j -= 1
        print(stack.pop())
        await asyncio.sleep(delay)

    event.set()

async def main():
    d1, d2, d3, j = map(int, input().split(','))
    q, st, e = asyncio.Queue(), [], asyncio.Event()
    await asyncio.gather(writer(q, d1, e), writer(q, d2, e),stacker(q, st, e), reader(st, j, d3, e))

asyncio.run(main())