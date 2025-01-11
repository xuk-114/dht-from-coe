n = int(input())
a =list(map(int,input().split()))
b = [0] +a +[0]
b[n+1] = -(b[n-1]-b[n])
if n == 1:
    print(1)
else:
    dp = [1]*(n+2)
    for i in range(2,n+1):
        for j in range(1,i):
            if j == 1:
                if b[i] != b[1]:
                    dp [i] = max(dp[i],2)
            elif (b[j-1]-b[j])*(b[j]-b[i]) < 0 :
                dp[i] = max(dp[j] +1,dp[i])
            else :
                dp[i] = max(1,dp[i])
print(max(dp))