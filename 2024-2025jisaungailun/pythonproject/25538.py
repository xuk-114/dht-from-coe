n = int(input())
x = bin(n)
c = x[2:]
a = list(map(str,c))
l = len(c)
b = list(map(str,c[::-1]))
for i in range(l):
    if a[i] != b[i]:
        print('No')
        exit()
print('Yes')
