import math
def euler(n):
    prime = [1] * (n+1)
    is_prime = []
    for i in range(2,n+1):
        if prime[i] == 1:
            is_prime.append(i)
        for j in is_prime:
            if i*j > n :
                break
            prime[i*j] = 0
            if i % j == 0:
                break
    return is_prime
s = euler(1000000)
input()
b = list(map(int,input().split()))
def judge(i):
    for j in s:
        if j ==int(math.sqrt(i)) and int(math.sqrt(i))**2==i :
            return True
result = []
for i in b:
    if i < 4:
        result.append('NO')
        continue
    elif int(i**0.5)**2 != i:
        result.append('NO')
        continue
    if int(i**0.5) in s:
        result.append('YES')
    else:result.append('NO')
print('\n'.join(result))

