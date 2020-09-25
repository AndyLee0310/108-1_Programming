"""
輸入 N ，之後輸入 N 個整數， 例如N=5，5個整數 11, 45, 8, 13, 22。
輸出其中第二大的數
輸出最大的數與最小的數相乘的結果。

Sample Input
3
1
2
3

Sample Output
2
3
"""
def getMaxMin(N): 
    my_list = []
    num = int(input()) 
    my_list.append(num)
#    maxValue= minValue= num; 
    for i in range(N-1): 
        num = int(input())
        my_list.append(num)
    newlist = sorted(my_list)
#    print(newlist)
    print(newlist[-2])      #印出第二大最大數值
#    print(max(my_list))     #印出最大數值
#    print(min(my_list))     #印出最小數值
    maxnum = max(my_list)
    minnum = min(my_list)
    newnum = maxnum * minnum
    print(newnum)


num = int(input()) 
getMaxMin(num) 