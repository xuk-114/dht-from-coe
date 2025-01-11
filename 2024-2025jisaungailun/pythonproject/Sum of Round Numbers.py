t = int(input())
b = 0
for i in range(t):
    b =input()
    c =len(b)
    n = 0
    for k in range(c):
        if int(str(b)[k]) != 0:
            n += 1
    print(n)
    for k in range(c):
        if int(str(b)[k]) != 0:
            d = int(str(b)[k]) * 10**(c-k-1)
            print(d,end=" ")

