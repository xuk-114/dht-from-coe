n = int(input())
s = input()
a = 0
for i in range(n-1):
    current = s[i]
    next = s[i+1]
    if current == next:
        a += 1
print(a)
