a = list(map(int,input().split()))
min_price = float('inf')
ans = 0
for i in a:
    min_price = min(min_price,i)
    ans = max (ans,i-min_price)
print(ans)