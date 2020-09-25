'''
撲克牌四種花色分別是黑桃、紅心、磚塊、梅花，定義 S, H, D, C。
牌面數字 2 ~ 14，A 為 14，J 為 11， Q 為 12，K 為 13，共有52張牌。
花色大小：黑桃>紅心>方塊>梅花。

編碼規則為數字+花色，例如 10S 表黑桃 10、7D 表磚塊 7，12C 表梅花 Q。

牌型由小到大如下：

散牌 -> 撲克牌遊戲把單一張牌命名為單張，沒有任何花色牌型，編號 0。
一對 -> 兩張數字一樣的命名為 Pair，編號 1。
兩對 -> 2 組 Pair 的牌稱為 Two pair，編號 2。
三條 -> 三張一樣數字的稱為 Three of a Kind，編號 3。
順子 -> 數字連續的 5 張牌稱為 Straight，包括 13 ,14, 2, 3, 4 或 12, 13 ,14, 2, 3 等，編號 4。
同花 -> 五張同一花色的牌稱為 Flush，編號 5。
葫蘆 -> Three of a Kind 加一個 Pair 稱為 Full House，編號 6。
四條 -> 四張一樣數字稱為 Four of a Kind，編號 7。
同花順 -> 數字連續的 5 張且花色一樣稱為 Straight Flush，編號 8。

輸入5張撲克牌，判斷哪一類型的牌形編號(0~8)。

輸入說明 ：
第一列輸入為5個編碼分別由空格分開，表示5張撲克牌。

輸出說明 ：
輸出為一個0~8的整數，代表牌型編號；注意要以「最大的牌型為輸出」。
數字連續的定義為：K(13) 和 A(14) 有相連，A(14) 和 2 有相連，依此類推。

Input:
-------------------------
9D 8C 8S 8H 9S 

Output
------------------------
6
'''
x = []
n=input().split()
def judge(x):
    Dict = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:3,12:4,13:5,14:6}
    tmp_X = x.copy()
    tmp_Y = []
    for i in x:tmp_Y.append(i[0])
    tmp_X.sort(key=lambda c:c[0])
    tmp_Y.sort()
    if tmp_Y[0] == 2 and tmp_Y[-1] == 14:
        for i in range(5):tmp_Y[i]=Dict[tmp_Y[i]]

    if tmp_Y[0]+4 == tmp_Y[1]+3 == tmp_Y[2]+2 == tmp_Y[3]+1 == tmp_Y[4] and tmp_X[0][1] == tmp_X[1][1] == tmp_X[2][1] == tmp_X[3][1] == tmp_X[4][1]:
        return 8
    for i in range(2):
        if tmp_X[i][0] == tmp_X[i+1][0] == tmp_X[i+2][0] == tmp_X[i+3][0]:
            return 7
    if (tmp_X[0][0] == tmp_X[1][0] == tmp_X[2][0] and tmp_X[3][0] == tmp_X[4][0]) or (tmp_X[2][0] == tmp_X[3][0] == tmp_X[4][0] and tmp_X[0][0] == tmp_X[1][0]):
        return 6
    if tmp_X[0][1] == tmp_X[1][1] == tmp_X[2][1] == tmp_X[3][1] == tmp_X[4][1]:
        return 5
    if tmp_Y[0]+4 == tmp_Y[1]+3 == tmp_Y[2]+2 == tmp_Y[3]+1 == tmp_Y[4]:
        return 4
    for i in range(3):
        if tmp_X[i][0] == tmp_X[i+1][0] == tmp_X[i+2][0]:
            return 3
    for i in range(2):
        if tmp_X[i][0] == tmp_X[i+1][0] and tmp_X[i+2][0] == tmp_X[i+3][0]:
            return 2
    for i in range(4):
        if tmp_X[i][0] == tmp_X[i+1][0]:
            return 1
    return 0
for i in n:x.append([int(i[0:-1]),i[-1]])
print(judge(x))