# (10a + k)*k = (10^d)*k + a
# (10a + k) is N
# d is amount of digits in a

k = int(input())

if k == 0:
    print(0)
elif k == 1:
    print(1)
else:
    z = 10 * k - 1

    #10d % z = k % z
    d = 1
    m = 10 % z
    while m != k % z:
        m = (10*m) % z
        d += 1
    a = k * (10**d - k) // z
    N = 10*a + k

    print(N)