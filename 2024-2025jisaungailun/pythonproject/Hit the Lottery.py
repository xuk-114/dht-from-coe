a = int(input())
b = a // 100
c = (a-100*b)//20
d = (a-100*b-20*c)//10
e = (a-100*b-20*c-10*d)//5
f = (a-100*b-20*c-10*d-5*e)//1
print(b+c+d+e+f)