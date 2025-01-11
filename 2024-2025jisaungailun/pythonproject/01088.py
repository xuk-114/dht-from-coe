r,c = map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(r)]
dp = [[-1]*c for _ in range(r)]
dx= [0,0,1,-1]
dy= [1,-1,0,0]
def dfs (x,y):
    if dp[x][y] != -1:
        return dp[x][y]
    max_length = 1
    for i in range(4):
         nx,ny = x+dx[i],y+dy[i]
         if 0<= nx<r and 0<=ny<c and matrix[nx][ny] < matrix[x][y]:
             max_length = max(max_length,1+dfs(nx,ny))
    dp[x][y] = max_length
    return dp[x][y]
result = 0
for i in range(r):
    for j in range(c):
        result = max(result,dfs(i,j))
print(result)