n, k = int(input()), int(input())
a = str(k)
ind = a[0]
if a.count(ind) == len(a):
    print(int(ind) * len(a))
else:
    print(k)