'''
請先輸入一個數n，
該數n決定後面要輸入幾個區間，
將第n個區間插入第1~n-1個區間，
並輸出最後結果。

範例輸入說明:
假設輸入n = 3
後面接著輸入三個區間，
1,3
6,9
2,5

範例輸出說明:
因2~5與6~9沒有交集，所以6,9不變
但1~3與2~5有交集，所以把2,5插入1~3中
則結果為1,5
所以最後輸出為:
1,5
6,9

sample input:
3
1,3
6,9
2,5

sample output:
1,5
6,9

------------------------------------
sample input2:
6
1,2
3,5
6,7
8,10
12,16
4,8

sample output2:
1,2
3,10
12,16

3,5 與 6,7 與8,10 它們與4,8皆有交集
但因6,7已在4,8中，所以它可忽略
且4,8剛好在3,5與8,10之間，
所以合併為3,10

'''
def test():
    num = int(input())
    list_A = []
    list_B = []
    for i in range(num):
        numbers = input().split(',')
        if i<num-1:
            list_A.append(numbers)
        else:
            setx = {x for x in range (int(numbers[0]),int(numbers[1])+1)}
            for j in list_A:
                sety = {y for y in range(int(j[0]),int(j[1])+1)}
                if setx & sety:
                    setx = setx|sety
                else:
                    list_B.append([int(j[0]),int(j[1])])
    z = [min(setx),max(setx)]
    list_B.append(z)
    list_B.sort()
    for inter in list_B:
        print(str(inter[0])+','+str(inter[1]))
test()