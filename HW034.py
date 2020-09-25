'''
計算最大公因數 GCD
給予三個整數，請計算出三個整數的最大公因數。

輸入說明:
一行三個整數以空格隔開，直到-1結束

輸出說明:
輸出三個整數的最大公因數。

Sample Input
18 9 6
21 42 63
-1

Sample Output
3
21
'''
def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n,m%n)

def test():
    while(True):
        num = input()
        num = num.split(' ')
        if num[0] == '-1':
            break
        else:
            a = gcd(int(num[0]),int(num[1]))
            b = gcd(int(num[1]),int(num[2]))
            c = gcd(a,b)
            print(c)
test()