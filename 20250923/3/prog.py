lsts1 = [list(map(int, input().split(',')))]
size = len(lsts1[0])
for _ in range(size - 1):
    lsts1.append(list(map(int, input().split(','))))
lsts2 = []
for _ in range(size):
    lsts2.append(list(map(int, input().split(','))))

result = [[0] * size for _ in range(size)]
for i in range(size):
    for j in range(size):
        for k in range(size):
            result[i][j] += lsts1[i][k]*lsts2[k][j]
        print(result[i][j], end='')
        if j != (size - 1):
            print(',', end='')
    print()