a = input()
a_list =list(a)
b = len(a_list)
d = 0
for i in range(b):
    num = 0
    if i >= b-6:
        break
    for k in range(7):
        if a[i] == a[i+k]:
            num += 1
    if num >= 7 :
        d += 1
        print('YES')
        break
if d == 0:
    print('NO')
