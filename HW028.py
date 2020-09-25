"""
28. 撲克牌
A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
A~10 點數為 1~10，J, K, Q 為 0.5。

加總點數越接近 21 的贏；超過 21 ，爆掉且分數為 0。
總共有2位玩家在比大小，玩家一開始會有一張撲克牌，接著可以選擇要在拿一張撲克牌或是不要拿牌 就此停止，直到有一位玩家點數爆掉或是獲得5張撲克牌為止。

輸入說明 ：
X、Y，2位玩家一開始會有一張初始的牌，
先輸入玩家X的情形，再輸入玩家Y的情形
輸入: 1 A 1 2，
    代表玩家X要了一張撲克牌 翻看後看到這張樸克牌是A，
        玩家Y要了一張撲克牌 翻看後看到這張樸克牌是2
輸入: 0 0 ，代表玩家X、Y不在要牌，並結束牌局立刻進行結算。

有一位玩家爆掉的話or有一位玩家獲得5張撲克牌or兩位玩家都不再要牌，該局立刻結束，並進行點數計算

輸出說明：
第一行 為那位玩家獲勝
第二、三行 為2位玩家的分數，若爆掉則顯示 Bang!

-->本題本次不會有 平手 之情形<--

Sample Input：
A A
1 10 1 2
1 9 0
1 8 0

Sample Output：
Player Y is Winner
Player X $ Bang!
Player Y $ 3
"""
def findCard(a):
    points=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    num=[1,2,3,4,5,6,7,8,9,10,0.5,0.5,0.5]
    for i in range(13):
        if a==points[i]:
            s=num[i]
    return s

def myFunction(a):
    if a>21:
        a=0
    return a
def computeNum():
    a=input().split(" ")
    X=findCard(a[0])
    Y=findCard(a[1])
    for i in range(4):
        s=input().split(" ")
        if s[0] == '0' and s[1] == '0':
            break
        elif s[0] == '1' and s[2] == '0':
            X=X+findCard(s[1])
        elif s[0] == '0' and s[1] == '1':
            Y=Y+findCard(s[2])            
        elif (s[0] == '1') and (s[2] == '1'):
            X=X+findCard(s[1])
            Y=Y+findCard(s[3])
        X= myFunction(X)
        Y= myFunction(Y)
        if X == 0 or Y == 0:
            break           
    if X>Y:
        print("Player X is Winner")
    elif X<Y:
        print("Player Y is Winner")
    if X == 0:
        print("Player X $ Bang!")
    else:
        print("Player X $",X)
    if Y == 0:
        print("Player Y $ Bang!")
    else:
        print("Player Y $",Y)
computeNum()