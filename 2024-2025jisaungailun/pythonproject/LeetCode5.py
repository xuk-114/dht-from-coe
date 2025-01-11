s= input()
n = len(s)
dp = [[0]*(n) for _ in range(n)]
ans = -1
for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if s[i] == s[i+1]:
        dp[i][i+1] = 1
        ans = max(ans,2)
for l in range(3,n+1):
    for i in range(n-l+1):
        j = i+l-1
        if s[i]==s[j] and dp[i+1][j-1]:
            dp[i][j] = 1
            ans = max(ans,l)
            left = i
            right = j
return s[left:right]
