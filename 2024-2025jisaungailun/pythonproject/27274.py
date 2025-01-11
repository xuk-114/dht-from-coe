s = input()
a = list(s)
n = len(a)
i = 0
while True:
    if 2 ** i<= n <2**(i+1):
        break
    i+=1
s_new = []
l = 0
r = i
while l<= r:
    if l == r:
        s_new.append(s[2**l -1])
    else:
        s_new.append(s[2**l-1])
        s_new.append(s[2**r-1])
    l +=1
    r -=1
print(''.join(map(str,s_new)))