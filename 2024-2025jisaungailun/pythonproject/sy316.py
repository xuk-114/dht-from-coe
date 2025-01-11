dx = [1,-1,0,0]
dy = [0,0,1,-1]
def is_valid(x,y):
    if not (0<=x<n and 0 <=y<m):
        return False
    if visited[x][y] == 1:
        return False
    return True
def dfs(x,y,step,way):
    global ans,ans_way
    if x == n-1 and y ==m-1:
        if step > ans:
            ans = step
            ans_way = way[:]
    visited[x][y] = 1
    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if is_valid(nx,ny):
            way.append((nx+1,ny+1))
            dfs(nx,ny,step+maze[nx][ny],way)
    way.pop()
    visited[x][y] = 0
n,m = map(int,input().split())
visited = []
maze = []
way = [(1,1)]
ans_way = []
ans =  -float('inf')
for _ in range(n):
    row = list(map(int,input().split()))
    maze.append(row)
visited = [[0]*m for _ in range(n)]
dfs(0,0,maze[0][0],way)
for x,y in ans_way:
    print(x,y)
