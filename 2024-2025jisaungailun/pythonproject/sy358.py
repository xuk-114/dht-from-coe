st = set()
def init():
    i = 1
    while i * i <= 1000000000:
        st.add(i * i)
        i += 1
def dfs(x):
    if x == len(i_d):
        return True
    c = 0
    for i in range(x,len(i_d)):
        c = c*10 + i_d[i]
        if c in st:
            if dfs(i+1):
                return True
    return False
n = int(input())
i_d =[]
while n:
    i_d.append(n%10)
    n //= 10
i_d.reverse()
init()
if dfs(0):
    print('Yes')
else:
    print('No')
