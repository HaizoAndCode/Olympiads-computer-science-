n, k = int(input()), int(input())
if (k % 11 == 0 and k < 100) or k % 111 == 0:
    print(k // 100 + k // 10 % 10 + k % 10)
else:
    print(k)