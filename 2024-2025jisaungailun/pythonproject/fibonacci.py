def f(i):
    if i == 1 or i == 2:
        return 1
    else:
        return f(i-1)+f(i-2)
print(f(int(input())))
