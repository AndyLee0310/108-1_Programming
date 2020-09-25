'''
小淞來到了第二關，等著他的又是一個巨大的迷宮。
這個二維整數陣列以1表示牆壁，0表示通道，構成一個巨大的迷宮。
迷宮的入口為迷宮第一行中，用直角方向(上u,下d,左l,右r)在迷宮中移動，想辦法從入口走到出口(只會有唯一解)。
除了入口和出口的部分，其餘邊界皆為牆壁(1)。
入口座標固定為(0,1)，出口座標為(1~N-2, M-1)任一點，如下所示：

N為5
M為7

1 0 1 1 1 1 1
1 0 0 0 0 0 1
1 0 1 0 1 1 1
1 0 1 0 0 0 0
1 1 1 1 1 1 1

給一個N×M的迷宮(3 <= N,M <= 9，N,M為奇數)，
挑戰者必須求出從入口走到出口的路徑
上例的解答輸出為drrddrrr

-----------------------------------------------
輸入說明：
輸入的第一行為列數 N，第二行為行數 M，
接下來 N 行每行代表迷宮的一行，含有以空白隔開的迷宮數字。

輸出說明：
對於每個迷宮，請輸出從入口走到出口的路徑。(以u,d,l,r表示)

-----------------------------------------------
範例輸入一

5
7
1 0 1 1 1 1 1
1 0 0 0 0 0 1
1 0 1 0 1 1 1
1 0 1 0 0 0 0
1 1 1 1 1 1 1

範例輸出一

drrddrrr

範例輸入二

5
7
1 0 1 1 1 1 1
1 0 0 0 1 0 0
1 0 1 0 1 0 1
1 0 1 0 0 0 1
1 1 1 1 1 1 1

範例輸出二

drrddrruur

'''
dicts=[['u',[0,-1]],['d',[0,1]],['l',[-1,0]],['r',[1,0]]]
x = int(input())
y = int(input())
array=[]
f=[]
mov=[]
for i in range(y):
    array.append([])
    f.append([])
for i in range(x):
    lines=input().split()
    for j in range(len(lines)):
        array[j].append(int(lines[j]))
        f[j].append(True)
haveAns=False
def getAns(col,row,a,b):
    global haveAns
    if a == row-1:
        print("".join(mov))
        haveAns = True
        return 
    for i in dicts:
        if col<=b+i[1][1]:
            continue
        if row<=a+i[1][0]:
            continue
        if array[a+i[1][0]][b+i[1][1]] == 0 and f[a+i[1][0]][b+i[1][1]]:
            f[a+i[1][0]][b+i[1][1]]=False
            mov.append(i[0])
            getAns(col,row,a+i[1][0],b+i[1][1])
            mov.pop()
            f[a+i[1][0]][b+i[1][1]]=True
        if haveAns == True:
            break
getAns(x,y,1,0)