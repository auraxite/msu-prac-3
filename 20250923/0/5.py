arr = eval(input())
for i in arr:
    if i % 2 == 1:
        print(i)
        break
else:
    print(arr[0])