"""
遞增等差數列

輸入說明
輸入三個整數a1、an、d。分別代表遞增等差數列的首項、末項、公差。

輸出說明
列出此遞增等差數列，以及此等差數列之和。

Sample input：
0 30 5

Sample output：
0 5 10 15 20 25 30
105

"""
def number(a1,an,d):
    num=0
    for i in range(a1,an+1,d):
        print(i,end=' ')
        num += i
    print()
    return num

allnum=input()
allnum=allnum.split(" ")
allnum=list(map(int,allnum))
print(number(allnum[0],allnum[1],allnum[2]))

"""
#另一種方式
def printNum():
    num = input()
    data = num.split(' ')
    a1 = int(data[0])
    an = int(data[1])
    d = int(data[2])
    num = 0 
    for i in range(a1,an+1,d):
        print(i,"",end='')
    print()
    for j in range(a1,an+1,d):
        num = num + j
        if j == an:
            print(num)
printNum()
"""
