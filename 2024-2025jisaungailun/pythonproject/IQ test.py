n = int(input())
num = list(map(int,input().split()))
even = 0
odd = 0
for i in range(n):
    if num[i] % 2 == 0:
        even += 1
        if even == 2:
            for k in range(n):
                if num[k] % 2 != 0:
                    print(k+1)
                    break
    elif num[i] % 2 != 0:
        odd += 1
        if odd == 2:
            for k in range(n):
                if num[k] % 2 == 0:
                    print(k+1)
                    break

