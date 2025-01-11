n,m = map(int,input().split())
store = [input().split() for _ in range(n)]
coupons = [input().split() for _ in range(m)]
shop = [[] for _ in range(n)]
def dfs(i):
    global result
    if i == n:

