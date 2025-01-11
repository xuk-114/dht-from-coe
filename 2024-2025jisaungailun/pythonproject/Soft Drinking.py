n,k,l,c,d,p,nl,np = map(int,input().split())
a = l * k // nl
b = p // np
q = c * d
m = min(a,b,q)
n = m // n
print(f'{n}')