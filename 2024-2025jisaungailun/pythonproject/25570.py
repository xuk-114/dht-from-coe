n = int(input())
mar = []
dir = [(0,1),(1,0),(0,-1),(-1,0)]
mar.append([-1]*(n+2))
for _ in range(n):
    row = list(map(int,input().split()))
    a = [-1] + row +[-1]
    mar.append(a)
mar.append([-1]*(n+2))
ans = -float('inf')
if n % 2 == 0:
    for i in range(n//2):
        sum = mar[i+1][i+1]
        mar[i+1][i+1] = -1
        s = q = i+1
        j = 0
        while True:
            l,r =dir[j]
            s += l
            q += r
            if mar[s][q]== -1:
                j+=1
                s-= l
                q-= r
                if j == 4:
                    ans = max(ans, sum)
                    break
            else:
                sum += mar[s][q]
                mar[s][q] = -1
else:
    for i in range(n//2 +1):
        sum = mar[i+1][i+1]
        mar[i+1][i+1] = -1
        s = q = i+1
        j = 0
        while True:
            l,r =dir[j]
            s += l
            q += r
            if mar[s][q]== -1:
                j+=1
                s -= l
                q -= r
                if j == 4:
                    ans = max(ans, sum)
                    break
            else:
                sum += mar[s][q]
                mar[s][q] = -1

print(ans)