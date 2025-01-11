n = int(input())
a = list(map(int,input().split()))
b = 0
c = 0
for i in range(n):
    if a[i] < 0 and c == 0:
        b += 1
    elif a[i] > 0 :
        c = c + a[i]
    else:
        c -= 1
print(b)


