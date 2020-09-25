"""
迴圈偶數連加，輸入兩整數a、b，且a 例如輸入 a=1、b=100，則輸出結果為 2550(2+4+6+8+ ... +100 =2550)
simple input:
1
100

simple output:
2550
"""

def cipher(a,b):
    num = 0
    for i in range(a,b+1):
        if i % 2 == 0:
            num += i
    print(num)
    
cipher(int(input()),int(input()))