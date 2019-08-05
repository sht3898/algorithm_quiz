def my_sqrt(n):
    a, b = 1, n
    result = 1
    while abs(result ** 2 - n) >= 1e-10:
        if (a + b/2) ** 2 < n:
            a += a/2
        else:
            b -= b/2
        result = b
    print(result)

my_sqrt(3)