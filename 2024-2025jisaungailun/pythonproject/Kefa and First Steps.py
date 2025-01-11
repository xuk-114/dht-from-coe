n = int(input())
a = list(map(int,input().split()))
c = 1
b = 1
if n == 1:
    print(1)
else:
    for i in range(len(a)-1):
        if a[i] <= a[i + 1]:
            c += 1
            if c >= b:
                b = c
        else:
            c = 1
    print(b)


