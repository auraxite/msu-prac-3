n = int(input())

i = n
while i <= n + 2:
    j = n
    while j <= n + 2:
        p = i * j

        s = 0
        tmp = p
        while tmp > 0:
            s += tmp % 10
            tmp //= 10

        print(i, "*", j, "=", ":=)" if s == 6 else p, end=" ")
        j += 1
    print()
    i += 1
