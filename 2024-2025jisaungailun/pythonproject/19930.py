from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def is_valid(x,y):
    if not (0<=x<m and 0 <=y<n):
        return False
    if maze[x][y] == 2:
        return False
    if (x,y) in inq:
        return False
    return True
def bfs(x,y,s):
    q = deque()
    q.append((x,y,s))
    inq.add((x,y))
    while q:
        x,y,s = q.popleft()
        if maze[x][y] == 1:
            return s
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if is_valid(nx,ny):
                inq.add((nx,ny))
                q.append((nx,ny,s+1))
    return -1
inq = set()
m, n = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(m)]
ans =bfs(0,0,0)
if ans == -1:
    print('NO')
else:
    print(ans)
