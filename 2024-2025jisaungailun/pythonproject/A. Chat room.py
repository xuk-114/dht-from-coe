import sys
def find(num):
    b = []
    for i in range(len(s)):
        if s[i] == num:
            b.append(i)
    if len(b) == 0:
        b.append(0)
    return b
s=list(map(str,input()))
h = find('h')
e = find('e')
l = find('l')
o = find('o')
e_0 = -1
for i in range(len(e)):
    e_0 = -1
    if h[0]< e[i]:
        e_0 = i
        break
if e_0 == -1:
    print('NO')
    sys.exit()
l_0 = -1
for i in range(len(l)-1):

    if e[e_0]<l[i]<l[i+1]:
        l_0 = i+1
        break
if l_0 == -1:
    print('NO')
    sys.exit()
if l[l_0]<o[-1]:
    print('YES')
else:print('NO')


