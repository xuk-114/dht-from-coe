def dfs(x,y):
    if matrix[x][y] == 9:
        print('yes')
        exit()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx <n and 0<=ny<n and (nx,ny) not in visited and matrix[nx][ny] != 1:
            if num == 1:
                if nx == n-1 or matrix[nx+1][ny] == 1:
                    continue
                if matrix[nx+1][ny] == 9:
                    print('yes')
                    exit()
            else:
                if ny == n-1 or matrix[nx][ny+1] == 1:
                    continue
                if matrix[nx][ny+1] == 9:
                    print('yes')
                    exit()
            visited.add((nx,ny))
            dfs(nx,ny)

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = set()
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 5:
            if i < n-1 and matrix[i+1][j] == 5:
                num = 1
            else:
                num = 2
            dfs(i,j)
            print('no')
            exit()
