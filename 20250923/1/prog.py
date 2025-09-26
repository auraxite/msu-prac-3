M, N = map(int, input().split(','))
print([i for i in range(M, N) if all(i % j != 0 for j in range(2, i))])