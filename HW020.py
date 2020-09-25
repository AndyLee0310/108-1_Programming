"""
範例輸入說明:
請輸入一個小於等於200的正整數，
並且判斷是否為質數。

範例輸出說明:
印出該整數，並且表示是否為質數

Sample Input:
137

Sample Output:
137 is prime number

Sample Input:
6

Sample Output:
6 is not prime number
"""

def judgenum(num):
    for i in range(200):
        newnum = num % 2
    if newnum == 0:
        print(num,'is not prime number')
    else:
        print(num,'is prime number')

judgenum(int(input()))