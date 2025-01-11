n,m,a = map(int,input().split())
c = min(n,m)
d = max(n,m)
def adov(num):
    if num % a == 0:
        return num // a
    elif num % a != 0:
        return (num //a)+ 1
n = adov(c)
m = adov(d)
print(f'{n*m}')