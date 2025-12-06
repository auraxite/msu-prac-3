import asyncio
import random

async def merge(A1, A2, s, m, f, e1, e2, eout):
    await e1.wait()
    await e2.wait()
    i, j, k = s, m, s

    while i < m and j < f:
        if A1[i] <= A1[j]:
            A2[k] = A1[i]; i += 1
        else:
            A2[k] = A1[j]; j += 1
        k += 1

    while i < m: A2[k] = A1[i]; i += 1; k += 1
    while j < f: A2[k] = A1[j]; j += 1; k += 1
    eout.set()

async def mtasks(A):
    n = len(A)
    B = [None]*n
    cur = A[:]
    nxt = B

    tasks = []
    events = [asyncio.Event() for _ in range(n)]
    for e in events:
        e.set()

    step = 1
    while step < n:
        new_events = []
        for i in range(0, n, 2*step):
            s, m, f = i, min(i+step,n), min(i+2*step,n)
            e1 = events[i//step]
            e2 = events[min(i//step+1, len(events)-1)]
            eout = asyncio.Event()
            tasks.append(asyncio.create_task(
                merge(cur, nxt, s, m, f, e1, e2, eout)
            ))
            new_events.append(eout)

        cur, nxt = nxt, cur
        events = new_events
        step *= 2

    return tasks, cur


import sys
code = sys.stdin.read()
exec(code, {"merge":merge, "mtasks": mtasks, "asyncio": asyncio, "random": random})