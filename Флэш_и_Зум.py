d, v1, v2, t = int(input("d= ")), int(input("v1= ")), int(input("v2= ")), int(input("t= "))
print(min(abs(v1 * t % d - v2 * t % d), d - abs(v1 * t % d - v2 * t % d)))