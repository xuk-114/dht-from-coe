dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt  = 0
n,m = map(int,input().split())
maze = []
ans =[]
for _ in range(n):
    row = list(map(int,input().split()))
    maze.append(row)
visited = [[False] *m for _ in range(n)]
def is_valid(x,y):
    if not (0 <= x<n and 0<= y<m):
        return False
    return not visited[x][y]
def dfs(maze,x,y,cnt):
    if x == n-1 and y == m-1:
        ans.append(cnt+maze[x][y])
    visited[x][y] = True
    for i in range(4):
        nx =x +dx[i]
        ny =y +dy[i]
        if is_valid(nx,ny):
            dfs(maze,nx,ny,cnt+maze[x][y])
    visited[x][y] = False
dfs(maze,0,0,0)
print(max(ans))
