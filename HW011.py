"""
撲克牌
A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
A~10 點數為 1~10，J, K, Q 為 0.5。
X, Y 兩個人各發三張撲克牌，加總點數越接近 10.5 的贏；超過 10.5 ，爆掉且分數為 0。
程式：
輸入：X, Y 兩個人的三張撲克牌。
輸出：兩個人的點數，以及A贏或B贏或平手。

Sample Input：
A
2
3
2
3
4
Sample Output：
6
9
B贏

Sample Input：
A
2
3
A
2
3
Sample Output：
6
6
平手

"""
def card_num(x):
    y=0
    if x=='A':
        y=num[0]
    elif x=='2':
        y=num[1]
    elif x=='3':
        y=num[2]
    elif x=='4':
        y=num[3]
    elif x=='5':
        y=num[4]
    elif x=='6':
        y=num[5]
    elif x=='7':
        y=num[6]
    elif x=='8':
        y=num[7]
    elif x=='9':
        y=num[8]
    elif x=='10':
        y=num[9]
    elif x=='J' or x=='Q' or x=='K':
        y=num[10]
    return y

A1=input()
A2=input()
A3=input()
B1=input()
B2=input()
B3=input()

num=[1,2,3,4,5,6,7,8,9,10,0.5]

newA1=card_num(A1)
newA2=card_num(A2)
newA3=card_num(A3)
newB1=card_num(B1)
newB2=card_num(B2)
newB3=card_num(B3)

newA=int(newA1+newA2+newA3)
newB=int(newB1+newB2+newB3)


if newA>10.5:
    newA=0
else:
    newA=newA
    
if newB>10.5:
    newB=0
else:
    newB=newB

if newA==newB:
    print(newA)
    print(newB)
    print('平手')
elif newA>newB:
    print(newA)
    print(newB)
    print('A贏')
elif newA<newB:
    print(newA)
    print(newB)
    print('B贏')