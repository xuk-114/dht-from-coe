n = int(input())
tree = []
cnt = 0
for _ in range(n):
    tree.append([int(i) for i in input().split()])
for i in range(1,n-1):
    p,h = tree[i]
    if p-h > tree[i-1][0]:
        cnt+=1
    elif p+h < tree[i+1][0]:
        cnt+=1
        tree[i][0] = p+h
if n == 1:
    print(1)
else:
    print(cnt+2)