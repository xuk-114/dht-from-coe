import heapq
dx=[0,0,1,-1]
dy=[1,-1,0,0]
m,n,p = map(int,input().split())
maze = [list(input().split()) for _ in range(m)]
anss = []
for _ in range(p):
    x_1,y_1,x_2,y_2 = map(int,input().split())
    ans = 'NO'
    if maze[x_1][y_1] != '#' and maze[x_2][y_2] != '#':
        dist = {(x_1,y_1):0}
        q = [(0,x_1,y_1)]
        while q:
            s,i,j = heapq.heappop(q)
            if i == x_2 and j ==y_2:
                ans = s
                break
            for k in range(4):
                di = i + dx[k]
                dj = j + dy[k]
                if 0<=di<m and 0<=dj <n and maze[di][dj] !='#':
                    cost = s + abs(int(maze[i][j]) - int(maze[di][dj]))
                    if (di,dj) not in dist or cost < dist[(di,dj)]:
                        dist[(di,dj)] = cost
                        heapq.heappush(q,(cost,di,dj))
    anss.append(ans)
for i in anss:
    print(i)