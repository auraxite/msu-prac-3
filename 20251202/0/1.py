def itersum(num, n):
    sum = []
    for i in range(n):
        y = yield f'{num} want int | {i}/{n}'

def task(num):
    n = yield f'{num} need n'
    res = yield from itersum(num, n)
    yield f'{n=}, {res=}. {sum(res)=}'

from collections import deque
tasks = (deque(task) for i in range(3))

def loop(tasks, n):
    for task in tasks:
        print(task)

    for i in range(n-1, 1, -1):
        try:
            task = tasks.pop(i % 7)
            print(task.send(i))
            tasks.append(task)
        except StopIteration() as E:
            print("One of them is Done")
            
loop(tasks, 30)