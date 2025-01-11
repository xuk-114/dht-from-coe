dx = [1,0]
dy = [0,1]
def dfs(x,y):
    global ans
    if x == m-1 and y ==n-1:
        ans+=1
    for i in range(2):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<m and ny <n:
            dfs(nx,ny)
m,n=map(int,input().split())
ans = 0
dfs(0,0)
print(ans)

