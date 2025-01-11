t = int(input())
for _ in range(t):
    total_1 = 0
    total_2 = 0
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_min = min(a)
    b_min = min(b)
    for k in range(n):
        total_1 = total_1 + a_min + b[k]
    for k in range(n):
        total_2 = total_2 + b_min + a[k]
    print(min(total_1,total_2))

