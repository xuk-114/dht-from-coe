n = int(input())
for _ in range(n):
    Q = [[] for _ in range(3)]
    for i in range(3):
        Q[i] = input().split()
    for j in 'ABCDEFGHIJKL':
                if all((j in i[0] and i[2] == 'up') or (j in i[1] and i[2] =='down') or
                       (j not in i[0] + i[1] and i[2] =='even') for i in Q):
                    print(f'{j} is the counterfeit coin and it is heavy. ')
                    break
                if all((j in i[1] and i[2] == 'up') or (j in i[0] and i[2] =='down') or
                       (j not in i[0] + i[1] and i[2] =='even') for i in Q):
                    print(f'{j} is the counterfeit coin and it is light. ')
                    break