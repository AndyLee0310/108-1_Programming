"""
計算總成績、平均:
某一學生修國文、計算機概論、計算機程式設計三科，使用者輸入名字（一個char）、學號（int）、三科成績(int)。
(1) 計算學生總成績、平均。
(2) 印出名字、學號、總成績、平均。

Input:
K
905067
100
100
100

Output:
Name:K
ID:905067
Average:100
Total:300
"""
a=input()
b=input()
c=input()
d=input()
e=input()
print('Name:',end='')   #{end=''}此為接續不空格
print(a)
print('ID:',end='')
print(b)
print('Average:',end='')
print(int((int(c)+int(d)+int(e))/3))
print('Total:',end='')
print(int(c)+int(d)+int(e))