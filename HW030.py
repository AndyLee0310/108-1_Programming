"""
030.數字排序

給定一串數字，將這一連串數字分為奇數在右，偶數在左，
並且奇數按照由小到大排，偶數按照由大到小排，

Input:
1 2 3 4 5 6 7 8 9

Output:
[1, 3, 5, 7, 9, 8, 6, 4, 2]
"""
def test():
    a,b=[],[]
    num = input()
    num=num.split(' ')
    num=list(map(int,num))
    num.sort()
#    print(num)
    for i in range(len(num)):
#        print(i)

        if num[i] % 2 == 0:
            a.append(num[i])
        else:
            b.append(num[i])
    a.sort(reverse=True)
    print(b+a)
test()