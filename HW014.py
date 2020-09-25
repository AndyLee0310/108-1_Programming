"""
輸入m, n 兩個整數，請計算等差為2的數列總和、等差為3的乘積，計算方式如下
1. m ~ n 之間 等差為2的和
m + (m+2) + (m+4) + (m+6) + ... + n
2. m ~ n 之間 等差為3的積
m * (m+3) * (m+6) * (m+9) * ... * n

Sample Input
2
10

Sample Output
30
80
"""

def totalsum(m,n):
    num = 0
    for i in range(m,n+1,2):
#        print(i)
        num = num + i
    print(num)

def totalmul(x,y):
    num1 = 1
    for a in range(x,y+1,3):
#        print(a)
        num1 = num1 * a
    print(num1)

m=int(input())
n=int(input())
totalsum(m,n)
totalmul(m,n)