t = int(input())
for _ in range(t):
    a = int(input())
    while a % 2 == 0:
        a = a // 2
    if a == 1:
        print('NO')
    else:
        print('YES')
