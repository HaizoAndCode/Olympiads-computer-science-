n, a, b = int(input("n= ")), int(input("a= ")), int(input("b= "))
for x in range(1, n + 1):
    s = a * (x+1) + (n - x) *b * 2
    list.append(s)
print(max(list))