n = int(input())
a = list(map(int,input().split()))
ans = [0]*100001
for i in a:
    ans[i] +=1
dp = [0]*100001
for i in range(1,100001):
    dp[i] = max(dp[i-1],dp[i-2]+ i * ans[i])
print(max(dp))