n = int(input())
t = list(map(int,input().split()))
dict_ = {}
for i in range(n):
    if t[i] not in dict_:
        dict_[t[i]] = [i+1]
    else:
        dict_[t[i]].append(i+1)
t.sort()
tol = 0
t_ = []
for i in t:
    if i not in t_:
        t_.append(i)
empy = []
for i in (t_):
    empy += dict_[i]
for i in range(n):
    tol += (n-i-1)*t[i]
result = tol / n
formatted = '{:.2f}'.format(result)
empy_str = [str(item) for item in empy]
print(' '.join(empy_str))
print(formatted)

