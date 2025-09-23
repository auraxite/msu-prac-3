list_even = eval(input())
if len(list_even) % 2 == 1:
    exit()

print(list_even[-2: len(list_even) // 2 :-2])