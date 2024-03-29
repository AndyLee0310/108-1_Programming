'''
042.對發票
阿銘是一個很喜歡對發票的男孩，這一個月他存了很多張發票，
如果要人工對發票，搞不好會漏掉千萬獎金，所以他想要寫一個
對發票的程式，請你們幫幫他吧!

發票對獎規則、獎金:
獎項-------------------條件-------------------金額

特別獎---------發票全號與特別獎號碼相同---------1000萬

特獎-----------發票全號與特獎號碼相同-----------200萬

頭獎-----------發票全號與頭獎號碼相同-----------20萬

二獎-----發票末7位號碼與頭獎號碼末7位號碼相同-----4萬

三獎-----發票末6位號碼與頭獎號碼末6位號碼相同-----1萬

四獎-----發票末5位號碼與頭獎號碼末5位號碼相同-----4千

五獎-----發票末4位號碼與頭獎號碼末4位號碼相同-----1千

六獎-----發票末3位號碼與頭獎號碼末3位號碼相同-----2百

增開六獎---發票末三位號碼與增開六獎號碼完全一樣----2百

輸入說明:
輸入的第一行為特別獎號碼(1組)，第二行為特獎號碼(1組)，第三行為頭獎號碼(3組)，第四行為增開六獎號碼(3組)，輸入對獎號碼後，輸入核對發票的筆數，再輸入核對發票的號碼。

輸出說明
輸出總累積獲得的獎金(一律寫數字，不能寫1百、千、萬....)
注意:以得獎金數最高為獎金，不能累計!例如:得二獎(末7碼)，代表三(末6碼)、四(末5碼)、五(末4碼)、六(末3碼)都有中，但是只能得二獎，以下的金額不能累計在內!

Sample Input
45698621
19614436
96182420 47464012 62781818
928 899 118
5
45698621
96182420
33364012
12341818
76588928

Sample Output
10205200
'''
x=[]
money=0
prize1= input()  #特別獎
prize2 = input()#特獎
prize3 = input().split()#頭獎
prize4 = input().split()#六獎
nums = int(input()) #輸入n張發票

for i in range(nums):
    x.append(input())
for j in range(len(x)):
    if x[j] == prize1:
        money+=10000000
    elif x[j] == prize2:
        money+=2000000
    elif x[j] == prize3[0] or x[j] == prize3[1] or x[j] == prize3[2]:
        money+=200000
    elif x[j][1:] == prize3[0][1:] or x[j][1:] == prize3[1][1:] or  x[j][1:] == prize3[2][1:]:
        money+=40000
    elif x[j][2:] == prize3[0][2:] or x[j][2:] == prize3[1][2:] or  x[j][2:] == prize3[2][2:]:
        money+=10000
    elif x[j][3:] == prize3[0][3:] or x[j][3:] == prize3[1][3:] or  x[j][3:] == prize3[2][3:]:
        money+=4000
    elif x[j][4:] == prize3[0][4:] or x[j][4:] == prize3[1][4:] or  x[j][4:] == prize3[2][4:]:
        money+=1000
    elif x[j][5:] == prize3[0][5:] or x[j][5:] == prize3[1][5:] or  x[j][5:] == prize3[2][5:]:
        money+=200
    elif x[j][5:] == prize4[0] or x[j][5:] == prize4[1] or x[j][5:] == prize4[2]:
        money+=200
print(money)