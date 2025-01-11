import math
n = int(input())
num = []
c = 0
for a in range(2,int(math.sqrt(n)+1)):
    while n % a == 0:
        num.append(a)
        n = n // a
if n > 1:
    num.append(n)
for i in num :
    if num.count(i) >= 2:
        c += 1
num_set = set(num)
length = len(num_set)
if c > 0:
    print(0)
else:
    if length % 2 == 0:
        print(1)
    else:
        print(-1)
    #计算质数时，为减少时间，可优化到2——根号n+1



