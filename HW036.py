'''
036

集合操作
給予兩集合，計算兩集合的運算的結果

輸入說明：
第一行輸入要輸入幾個字串
第二行輸入數個字串(以空格隔開)
第三行輸入運算子
第四行輸入要輸入幾個字串
第五行輸入數個字串(以空格隔開)

輸出說明：
輸出兩集合的運算後的結果，須以字典排序印出

注意運算子有:&、|、-、^、>、<、>=、<=、==

Sample Input
5
abc def ghi jkl mn
|
3
abc de jk

Sample Output
{'abc', 'de', 'def', 'ghi', 'jk', 'jkl', 'mn'}

逗點後須空一格
'''
numA = int(input())
wordA = set(input().split(' '))
x = input()
numB = int(input())
wordB = set(input().split(' '))

if x == '&':
    a = sorted(list(wordA & wordB))
    print("{'",end='')
    print("', '".join(a),end='')
    print("'}")
elif x == '|':
    a = sorted(list(wordA | wordB))
    print("{'",end='')
    print("', '".join(a),end='')
    print("'}")
elif x == '-':    
    a = sorted(list(wordA - wordB))
    if a == set():
        print("{",end='')
        print("}")
    else:
        print("{",end='')
        print("', '".join(a),end='')
        print("}")
elif x == '^':
    a = wordA ^ wordB
    print(a)
elif x == '>':
    a = wordA > wordB
    print(a)
elif x == '<':
    a = wordA < wordB
    print(a)
elif x == '>=':
    a = wordA >= wordB
    print(a)
elif x == '<=':
    a = wordA <= wordB
    print(a)
elif x == '==':
    a = wordA == wordB
    print(a)