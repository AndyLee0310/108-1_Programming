"""
輸入一字串，
1. 印出該字串中的小寫字母 (注意:若沒有字串中沒有小寫字母則輸出'No lowercase letters')
2. 計算該字串有幾個字元?
3. 計算該字串中大寫字元的數量

Sample Input
I have a pen, I have an apple.

Sample Output
haveapenhaveanapple
30
2
"""
def myStr():
    isupper = 0
    my_list=[]
    String=input()
    for index in String:
        if index.islower():
            my_list.append(index)
    if len(my_list) == 0:
        print('No lowercase letters')
    else:
        print(''.join(my_list))

    print(len(String))
    for index in String: 
        if index.isupper(): 
            isupper = isupper + 1
    print(isupper)

myStr()