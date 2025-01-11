def full_sort(n,ans=[],hash=None):
    if hash is None:
        hash = [False] * (n+1)
    if len(ans) == n:
        return [ans]
    result = []
    for i in range(1,n+1):
        if hash[i]:
            continue

        hash[i] = True
        result += full_sort(n,ans+[i],hash)
        hash[i] = False
    return result
n = int(input())
for p in full_sort(n):
    print(' '.join(map(str,p)))
