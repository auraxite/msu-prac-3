def Pareto(*tuples: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    i = 0
    arr = list(tuples)
    while i < len(arr):
        j = 0
        while j < len(arr):
            if i != j:
                if (arr[i][0] >= arr[j][0]) and (arr[i][1] > arr[j][1]) or \
                (arr[i][1] >= arr[j][1]) and (arr[i][0] > arr[j][0]):
                    arr.pop(j)
                    if i >= j:
                        i -= 1
                    j -= 1
            j += 1
        i += 1
    return tuple(arr)

print(*Pareto(*eval(s)), sep=', ') if (s := input().strip()) else None