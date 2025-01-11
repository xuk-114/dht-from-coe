while True:
    n = int(input())
    if n ==0:
        break
    tian = list(map(int,input().split()))
    king = list(map(int,input().split()))
    tian.sort(reverse=True)
    king.sort(reverse=True)
    c = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if tian[i-1] > king[j-1]:
                c[i][j] = max(c[i-1][j],c[i][j-1],c[i-1][j-1]+2)
            elif tian[i-1] == king [j-1]:
                c[i][j] = max(c[i-1][j],c[i][j-1],c[i-1][j-1]+1)
            else:
                c[i][j] = max(c[i-1][j],c[i][j-1],c[i-1][j-1])
    print((c[n][n]-n)*200)



