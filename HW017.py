"""
設計計算BMI值的Python function
BMI值計算公式: BMI = 體重(公斤) / 身高^2(公尺^2)
，例如：一個52公斤的人，身高是155公分
，則BMI為 : 52(公斤)/1.55^2 ( 公尺^2 )= 21.6。
正常範圍為BMI=18.5～24。
請設計一個 function，從鍵盤輸入姓名name、身高、體重。
當BMI太大，輸出 Hi name, Your BMI: xxx too HIGH.
當BMI太小，輸出 Hi name, Your BMI: xxx too LOW.
在正常範圍，輸出 Hi name, Your BMI: xxx.
註:BMI直接%f輸出即可。

Sample Input
Jeff
155
52

Sample Output
Hi Jeff, Your BMI: 21.644121.
"""

def BMI():
    name = input()
    m=int(input())
    kg=int(input())
    bmi = kg / (m/100) ** 2
    if bmi > 24:
        print('Hi',name + ', Your BMI:',"%f"%bmi + ' too HIGH.')
    elif bmi < 18.5:
        print('Hi',name + ', Your BMI:',"%f"%bmi + ' too LOW.')
    else:
        print('Hi',name + ', Your BMI:',"%f"%bmi + '.')

BMI()