import math
h,l,n = map(int,input().split())
v = list(map(int,input().split()))
t = []
for i in v:
    t.append(l / i)
t.sort()
le = len(t)
if le %2 == 0:
    time = t[(le // 2) -1]
else:
    time = t[(le-1) // 2]
s = 5 * time**2
x = h - s
print(f'{x:.2f}')
