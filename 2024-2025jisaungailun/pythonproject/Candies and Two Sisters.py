t = int(input())
b = 0
for _ in range(t):
    n = int(input())
    if n <= 2:
        print(0)
    else:
        if n % 2 == 0:
            b = n // 2 - 1
            print(b)
        else:
            b = n // 2
            print(b)

