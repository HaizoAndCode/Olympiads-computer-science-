d, v1, v2, t = int(input()), int(input()), int(input()), int(input())
print(min(abs(d - v1*t)+abs(d - v2*t), d - (abs(d - v1*t)+abs(d - v2*t))))