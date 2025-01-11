t = int(input())
ab = 0
def swap(a,b,list):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(n):
        for j in range(n):
            if j >= i:
                ab = abs(a[i]-b[j])
                if ab <=k:
                    swap(i,j,b)
                    break
    print(*b)



