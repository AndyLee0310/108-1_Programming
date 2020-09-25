"""
請使用 while loop或for loop
第一個輸入意義為選擇三種圖形:
1 三角形方尖方面向右邊
2 三角形方尖方面向左邊
3 菱形

第二個輸入意義為畫幾行
(奇數，範圍為 3,5,7,9,....,21)

input
1 (第一種圖形，三角形尖方面向右邊)
9 (共 9 行)
--------------------------
output
*
**
***
****
*****
****
***
**
*
---------------------------
input
2 (第二種圖形，三角形尖方面向左邊)
5 (共 5 行)
---------------------------
output
..*
.**
***
.**
..*
--------------------------
input
3 (第三種圖形: 菱形 )
3 (共 3 行數)

輸出
.*
***
.*
"""
def draw(a,t):
    newt = int(t / 2)
    if a == 1:
        for v in range(newt+1):
            for i in range(v+1):#根據外層行號，透過加1可以剛好等於星數
                print('*',end='')
            print('\n',end='')
        for v in range(newt):
            for i in range(newt-v):
                print('*',end='')
            print('\n',end='')
    elif a == 2:
        for v in range(newt):
            for j in range(newt-v):
                print('.',end='')
            for i in range(v+1):#根據外層行號，透過加1可以剛好等於星數
                print('*',end='')
            print('\n',end='')
        print('*'*(newt+1))
        for v in range(newt):
            for i in range(v+1):
                print('.',end='')
            for j in range(newt-v) :    
                print('*',end='')
            print('\n',end='')
    elif a == 3:
        for i in range(1,newt + 2):
            print('.'*(newt-i+1)+'*'*i+'*'*(i - 1))
        for i in range(newt,0,-1):
            print('.'*(newt-i+1)+'*'*i+'*'*(i - 1))

draw(int(input()),int(input()))