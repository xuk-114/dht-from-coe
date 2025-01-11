def change(k,s):
    ans = []
    for char in s:
        if 'a' <= char <='z':
            change_char = chr((ord(char) -ord('a') -k) %26 +ord('a'))
        elif 'A' <=char <='Z':
            change_char = chr((ord(char) -ord('A') -k) %26 +ord('A'))
        else:
            change_char = char
        ans.append(change_char)
    return ''.join(ans)
k = int(input())
s = input()
print(change(k,s))
