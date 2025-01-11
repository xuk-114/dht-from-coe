dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(maze,x,y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[nx][ny] == 'e':
            cnt += 1
            continue
        if maze[nx][ny] == 0:
            maze[x][y] = 1
            dfs(maze,nx,ny)
            maze[x][y] = 0
    return
n,m = map(int,input().split())
maze = []
maze.append([-1 for x in range(m+2)])
for _ in range(n):
    maze.append([-1] + [int(_) for _ in input().split()] + [-1])
maze.append([-1 for x in range(m+2)])
maze[1][1] = 's'
maze[n][m] ='e'
cnt = 0
dfs(maze,1,1)
print(cnt)
