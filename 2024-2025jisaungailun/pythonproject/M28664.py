n = int(input())
results=[]
for _ in range(n):
    a = list(input().strip())
    for i in range(len(a)-1):
        a[i] = int(a[i])
    if a[17] != 'X':
        a[17] = int(a[17])
    tol = a[0]*7+a[1]*9+a[2]*10+a[3]*5+a[4]*8+a[5]*4+a[6]*2+a[7]*1+a[8]*6+a[9]*3+a[10]*7+a[11]*9+a[12]*10+a[13]*5+a[14]*8+a[15]*4+a[16]*2
    b = tol % 11
    check_codes = {0: 1, 1: 0, 2: 'X', 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2}
    expect = check_codes[b]
    if expect == a[17]:
        results.append('YES')
    else:
        results.append('NO')
for i in results:
    print(i)