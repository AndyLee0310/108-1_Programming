"""
27.
給定一些線段，求這些線段所覆蓋的長度，注意，重疊的部分只能算一次。

輸入說明 ：
第一列輸入一個正整數 n: 代表共有 n 組測試案例。

接下來每一組測試案例的第一列是一個整數 m
表示此測試案例有m個線段，

接著的m列每一列是一個線段的兩端點，

每一個端點是一個整數介於0~60000之間，
端點之間以一個空格區隔，線段個數不超過 5000。

起始端點小的先輸入。

Sample Input：
5
1 5
5 10
10 15
15 20
19 25

Sample Output：
24
"""
def computeNum():
    n = int(input())
    a,b = [],[]
    length = 0
    for i in range(n):
        c = input().split()
        d = [int(x) for x in c]
        a.append(d)
    b = sorted(a)
    start = b[0][0]
    end = b[0][1]
    for i in range(n-1):
        if (b[i+1][0] <= end and b[i+1][1] <= end):
            continue
        elif (b[i+1][0] <= end and b[i+1][1] > end):
            end = b[i+1][1]
        elif (b[i+1][0] > end and b[i+1][1] > end):
            length = length + (end - start)
            start = b[i+1][0]
            end = b[i+1][1]
    length = length + (end - start)
    print(length)
computeNum()