def insertion_sort(lst: list, get_key) -> list:
    for i in range(1, len(lst)):
        val = lst[i]
        key = get_key(lst[i])
        j = i - 1
        while (j >= 0) and (get_key(lst[j]) > key):
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = val
    return lst

lst = list(map(int, input().split(',')))
# print("keys: ", ', '.join(str((el**2 % 100)) for el in lst))

print(insertion_sort(lst, lambda x: x**2 % 100))