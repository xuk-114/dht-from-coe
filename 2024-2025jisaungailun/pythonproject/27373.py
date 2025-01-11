m = int(input())
n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)

l = []
for k in a:
    l.append(len(str(k)))
dp = [['']*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if l [i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp [i][j] =max(dp)