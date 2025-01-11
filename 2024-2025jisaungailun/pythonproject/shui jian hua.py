a,b = map(int,input().split())
num = []
tol = 0
for i in range(a,b+1):
    t = i
    n_1 = i % 10
    i = i // 10
    n_2 = i % 10
    i = i // 10
    n_3 = i % 10
    if t == n_1 ** 3 + n_2 ** 3 + n_3 ** 3:
        num.append(t)
        tol += 1
if tol != 0:
    print(' '.join(map(str,num)))
elif tol == 0:
    print('NO')