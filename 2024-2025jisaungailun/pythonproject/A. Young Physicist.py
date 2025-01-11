n = int(input())
cnt_x = 0
cnt_y = 0
cnt_z = 0
for _ in range(n):
    a,b,c = map(int,input().split())
    cnt_x += a
    cnt_y += b
    cnt_z += c
if cnt_x == 0 and cnt_y == 0 and cnt_z == 0:
    print('YES')
else:print('NO')