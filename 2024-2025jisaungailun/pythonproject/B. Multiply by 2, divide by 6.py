t =int(input())
for _ in range(t):
    cnt = 0
    n =int(input())
    while n % 6 == 0:
        cnt+=1
        n = n // 6
    while n % 3 == 0:
        n = n*2
        n = n//6
        cnt+=2
    if n == 1:
        print(cnt)
    else:print('-1')






