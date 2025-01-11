num_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
num_dict_1 = [('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]
num_dict_2 = {'V':4,'X':9,'L':40,'C':90,'D':400,'M':900}
num = ['I','V','X','L','C','D','M']
b = []
s = input()
tol = 0
flag = 1
for i in num:
    if s[0] == i:
        flag = 2
        break
if flag == 2: #从罗马到数字
    tem_ro = num_dict[s[0]]
    for i in range(len(s)-1):
        if tem_ro>=num_dict[s[i]] >= num_dict[s[i+1]]:
            tol += num_dict[s[i]]
        elif tem_ro < num_dict[s[i]]:
            continue
        else:
            tol = tol + num_dict_2[s[i+1]]
        tem_ro = num_dict[s[i]]
    if num_dict[s[-1]] <= tem_ro:
        tol += num_dict[s[-1]]
    print(tol)
else:#从数字到罗马
            s = int(s)
            for roman,value in num_dict_1:
                while s >= value:
                    b.append(roman)
                    s -= value
            print(''.join(b))



