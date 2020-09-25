"""
041.午餐吃什麼?

國立台北科技大學坐落於車水馬龍的忠孝東路，
可以遠眺台北101，俯視光華商場，坐擁圓山飯店，
每到中午要吃什麼變成所有學生的困擾，
請寫一個投票程式，給大家選項、投票，
選出今天中午要吃什麼!

輸入說明:
輸入整數n代表有n個店家，
輸入n個店家的名稱(一個一行)包含空格、特殊字元，如:Guanhua Digital Plaza
接著輸入整數m代表有m個人投票，
輸入m行投票選項(如:5代表投第5個店家)

輸出說明:
印出最高票的店家及票數
註:不會有平票的狀況

Sample Input
5
PASTA
7-ELEVEN
Seafood restaurant
Dessert shop
Ba Fang Yun Ji Dumpling
5
1
2
3
5
5

Sample Output
Ba Fang Yun Ji Dumpling 2
"""
eats = []
listnum=[]
c,d = [],[]

num = int(input())
for i in range(0,num,1):
    x = input()
    eats.append(x)

n = int(input())
for a in range(0,n,1):
    b = int(input())
    listnum.append(b)
setnum=set(listnum)

for each_set in setnum:
    count = 0
    for each_list in listnum:
        if each_set == each_list:
            count += 1
        c.append(count)
        d.append(each_set)
maxc = max(c)
cc = c.index(maxc)
print(eats[d[cc]-1],end=' ')
print(maxc)