import math
l = 5
total = 0
while True:
    l = float(input())
    if math.isclose(l,0.00,rel_tol=1e-9):
        break
    i = 1
    total = 0
    while True:
        total += (1/(i+1))
        if l < total:
            print(f'{i} card(s)')
            break
        i += 1




