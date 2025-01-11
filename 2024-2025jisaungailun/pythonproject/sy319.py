from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    q = deque([x,y])
    inq.add((x,y))
    while q:
        front = q.popleft()
        for i in range(4):
            nx = front[0] + dx[i]
            ny = front[1] + dy[i]
            if maze[nx][ny] == 1 and (nx,ny) not in inq:
                inq.add(nx,ny)
                q.append((nx,ny))
n,m =map(int,input().split())
maze = [[-1]*(m+2)] + [[-1] + list(map(int,input().split())) + [-1] for _ in range(n)] + [[-1]*(m+2)]
counter = 0
inq = set()
for i in range(1,n+1):
    for j in range(1,m+1):
        if maze[i][j] == 1 and(i,j) not in inq:
            bfs(i,j)
            counter += 1
print(counter)