Haab = {"pop": 0, "no": 1, "zip": 2, "zotz": 3, "tzec": 4, "xul": 5, "yoxkin": 6, "mol": 7, "chen": 8, "yax": 9, "zac": 10, "ceh": 11, "mac": 12, "kankin": 13, "muan": 14, "pax": 15, "koyab": 16, "cumhu": 17}
Tzolkin = {0: "imix", 1: "ik", 2: "akbal", 3: "kan", 4: "chicchan", 5: "cimi", 6: "manik", 7: "lamat", 8: "muluk", 9: "ok", 10: "chuen", 11: "eb", 12: "ben", 13: "ix", 14: "mem", 15: "cib", 16: "caban", 17: "eznab", 18: "canac", 19: "ahau"}
day_to ={}
i=0
j = 0
k = 0
b = []
while k <= 260:
    if i >= 20: i = i%20
    if j >= 13: j = j%13
    day_to[k] = f'{j+1} {Tzolkin[i]} '
    k+=1
    i+=1
    j+=1
n = int(input())
for _ in range(n):
    s=[]
    text = input()
    parts = text.split()
    for char in parts[0]:
        if char !='.':
            s.append(char)
    day = ''.join(s)
    day = int(day)
    month =parts[1]
    year = int(parts[2])
    if month =='uayet':
        tol_day = year*365+360+day
    else:
        tol_day = year*365+Haab[month]*20+day
    year_T = tol_day // 260
    b.append(f'{day_to[tol_day%260]}{year_T}')
print(n)
for i in b:
    print(i)

