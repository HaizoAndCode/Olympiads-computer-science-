n, k = int(input()), int(input())
if k % 11 == 0 or k in [1, 2, 3, 4, 5, 6, 7, 8, 9] or k % 111 == 0:
    print(k // 100 + k // 10 % 10 + k % 10)
else:
    print(k)