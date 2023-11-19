n, m, k, t = int(input()), int(input()), int(input()), int(input())
if (m + t) % k >= 0:
    print(n + m - (m + t) // k * k)
else:
    print(n)