t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    n = 0
    c = 0
    if a % b == 0:
        print('0')
    else:
        c = (a // b) + 1
        n = (c * b) - a
        print(n)


