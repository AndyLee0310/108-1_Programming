'''
費氏數列 Fibonacci number

請用遞迴撰寫。
輸入一個整數n，輸出 Fibonacci number。

F(1) = 1 ; F(2) = 1;
F( n ) = F(n-1) + F(n-2) ;n > 2

輸入說明：

每一組一個正整數，輸入-1結束所有輸入。
數字代表第幾個數列的數字 1~100

輸出說明：

費氏數列的值。

---------------------

Sample Input:

1
2
5
-1

Sample Output:

1
1
5
'''
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
def mean():
    while(True):
        num = input()
        if num == '-1':
            break
        else:
            print(fibo(int(num)))
mean()