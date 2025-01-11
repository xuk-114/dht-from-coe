b = 0
c = 0
for i in range(5):
    new = list(map(int,input().split()))
    for k in range(5):
        if new[k] == 1:
            b= i+1
            c= k+1
d = abs(b-3)+abs(c-3)
print(d)
