a =list(map(int,input().split()))
b =max(a)
for i in a:
    if b - i != 0:
        print(b-i)