a , b=map(int,input().split())
c = a * b
if c % 2 == 0:
    c = c // 2
    print(f'{c}')
else:
    c = c - 1
    c = c // 2
    print(f'{c}')

