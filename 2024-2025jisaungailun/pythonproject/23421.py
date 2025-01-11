n,b = map(int,input().split())
prices = list(map(int,input().split()))
weights = list(map(int,input().split()))
bag = [0] * (b+1)
for i in range(n):
    for j in range(b,weights[i]-1,-1):
        bag[j] = max(bag[j],bag[j-weights[i]]+prices[i])
print(bag[-1])