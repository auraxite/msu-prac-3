arr = []
while l := input():
    el = list(eval(l))
    arr.append(el)

if any(len(l) == len(arr) for l in arr):
    for y in range(len(arr)):
        for x in range(y + 1, len(arr[y])):
            arr[x][y], arr[y][x] = arr[y][x], arr[x][y]
    for line in arr:
        print(*line, sep=", ")
else:
    print("not square")