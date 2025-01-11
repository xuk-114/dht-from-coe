t = int(input())
for _ in range(t):
    n = int(input())
    sum = 0
    i = 0
    while True:
        if 2**(i) <= n < 2**(i+1):
            break
        i +=1
    sum = (1+n)*n//2 - 2 * (2**(i+1) -1)
    print(sum)