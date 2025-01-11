dx = [-1,1,0,0]
dy = [0,0,-1,1]
flaga = False
def dfs(maze,x,y,step):
    global flaga
    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if maze[nx][ny] == 'e':
            if step == k-1:
                flaga = True
                return
            continue
        if maze[nx][ny] == 0:
            if step < k:
                maze[x][y] = -1
                dfs (maze,nx,ny,step+1)
                maze[x][y] = 0
n,m,k = map(int,input().split())
maze = []
maze.append([-1 for _ in range(m+2)])
for _ in range(n):
    maze.append([-1] + [int(_) for _ in input().split()] + [-1])
maze.append( [-1 for x in range(m+2)] )
maze[1][1] = 's'
maze[n][m] = 'e'
dfs(maze,1,1,0)
print('YES' if flaga else 'NO')
