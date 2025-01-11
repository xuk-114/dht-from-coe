n,a,b =map(int,input().split())
trees = list(map(int,input().split()))
i = 0
j = n-1
wat_a = a
num = 0
wat_b = b
while i <= j:
    if i==j:
        if wat_b>wat_a:
            if trees[j] <= wat_b:
                wat_b -= trees[j]
            else:
                num += 1
                wat_b = b - trees[j]
        else:
            if trees[i] <= wat_a:
                wat_a -= trees[i]
            else:
                num += 1
                wat_a = a - trees[i]
    else:
        if trees[i] <= wat_a:
            wat_a -= trees[i]
        else:
            num += 1
            wat_a = a -trees[i]
        if trees[j] <= wat_b:
            wat_b -= trees[j]
        else:
            num += 1
            wat_b = b - trees[j]
    i += 1
    j -= 1
print(num)