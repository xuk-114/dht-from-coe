n = int(input())
ans = 0
for i in range(n):
    ans += (input().replace('### ###',' ')).count('###')//2
print(ans)