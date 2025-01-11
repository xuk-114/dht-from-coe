kb ='qwertyuiopasdfghjkl;zxcvbnm,./'
d = input()
s = input()
if d == 'R':
    ans =''.join(kb[kb.index(c)-1]for c in s)
else:
    ans =''.join(kb[kb.index(c)+1]for c in s)
print(ans)