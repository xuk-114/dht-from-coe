def judge(n,m):
    if n % m == 0:
        return n // m
    else:
        return n//m +1
n = int(input())
peo = list(map(int,input().split()))
n_1 = peo.count(1)
n_2 = peo.count(2)
n_3 = peo.count(3)
n_4 = peo.count(4)
tol = 0
tol += n_4
if n_1>=(n_3 + n_2*2):
    remain = judge(n_1 -(n_3 + n_2*2),4)
    tol = tol +n_2+n_3+remain
    print(tol)
elif (n_3 + n_2*2)>n_1>= n_3:
    c = n_1 -n_3
    remain = judge(c,2)
    d = n_2 - remain
    remain_2 = judge(d,2)
    tol = tol + n_3 + remain_2 +remain
    print(tol)
else:
    remain = judge(n_2,2)
    tol = tol + n_3 + remain
    print(tol)





