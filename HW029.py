"""
29.
《孫子算經》裡有個「物不知其數」的問題：「今有物，不知其數，三三數之賸二，五五數之賸三，七七數之賸二。問物幾何？
幫你們翻譯：眼前有一堆物品，不知有多少個。每次取3個，最後剩下2個；每次取5個，最後剩下3個；每次取7個，最後剩下2個。問這堆物品到底有多少個？。

輸入說明：
每次取x1個，最後剩下y1個；每次取x2個，最後剩下y2個；每次取x3個，最後剩下y3個
輸入正整數 x1,y1,x2,y2,x3,y3

輸出說明：
這堆物品到底有多少個

Sample Input：
3 2 5 3 7 2

Sample Output：
23
"""
def number(x):
    num = x.split(' ')
    num = list(map(int,num))
    numbera,numberb,numberc,i = 0,0,0,0
    while(True):
        i += 1
#       print(i)
        if (i-num[1])%num[0]==0:
            numbera = i
            if (i-num[3])%num[2]==0:
                numberb = i
                if (i-num[5])%num[4]==0:
                    numberc = i
        if i==numbera==numberb==numberc:
            print(i)
            break
number(input())