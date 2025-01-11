pig = []
d = []
while True:
    try:
        a = input().split()
        if a[0] == 'push':
           t = int(a[1])
           pig.append(t)
           if not d :
               d.append(t)
           else:
               d.append(min(t,d[-1]))
        elif a[0] == 'min':
            if pig:
                print(d[-1])
        else :
            if pig:
                pig.pop()
                if d:
                    d.pop()
    except EOFError:
        break
