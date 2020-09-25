"""
檢查三門課程是否衝堂，
依序輸入課程編號(數字)、
上課小時數(1-3小時)、
上課時間(星期1-5, 第1-9節)

輸入說明
1001 (第一門課課程編號)
3 (3小時)
11 (星期1 第1節課)
59 (星期5 第9節課)
25 (星期2 第5節課)
2020 (第二門課課程編號)
2
25
16
2030 (第三門課課程編號)
…

輸出說明 (兩課程編號衝突在哪幾節)
1001 and 2020 conflict on 25

Sample Input：
1001
3
11
12
13
1002
3
21
22
23
1003
3
31
32
13
Sample Output：
1001 and 1003 confict on 13
"""
def classtime(x):
    if x==3:
        day1 = int(input())
        day2 = int(input())
        day3 = int(input())
        return[day1,day2,day3]
    elif x==2:
        day1 = int(input())
        day2 = int(input())
        return[day1,day2]
    elif x==1 :
        day1 = int(input())
        return[day1]
        
def function(a,b,c,d):
    set1 = set(c)
    set2 = set(d)
    f = list(set1.intersection(set2))
    if len(f)==3:
        print(a + ' and ' + b + ' confict on ' + str(f[0]))
        print(a + ' and ' + b + ' confict on ' + str(f[1]))
        print(a + ' and ' + b + ' confict on ' + str(f[2]))
    elif len(f)==2:
        print(a + ' and ' + b + ' confict on ' + str(f[0]))
        print(a + ' and ' + b + ' confict on ' + str(f[1]))
    elif len(f)==1:
        print(a + ' and ' + b + ' confict on ' + str(f[0]))
        
classnum1 = input()
time1=classtime(int(input()))
classnum2=input()
time2=classtime(int(input()))
classnum3=input()
time3=classtime(int(input()))
function(classnum1,classnum2,time1,time2)
function(classnum1,classnum3,time1,time3)
function(classnum2,classnum3,time2,time3)
