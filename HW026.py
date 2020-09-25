"""
計算出最小公倍數

輸入說明：
兩個正整數

輸出說明：
這兩個正整數的最小公倍數。

Sample input：
2
3

Sample output：
6


((維基百科，最小公倍數：
https://zh.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B8
"""
def number(x,y):
    if x > y :
        maxnum = x
    else:
        maxnum = y
    while(True):
        if ((maxnum % x == 0) and (maxnum % y == 0)):
            lcm = maxnum
            break
        maxnum += 1
    print(lcm)
    
x = int(input())
y = int(input())
number(x,y)