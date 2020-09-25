'''
給定兩個字串，A為父字串，B為子字串，
請在A中找出最短字串C，
且B必須為C的子集。

範例輸入說明:

M = CDEBATC
S = ABC

範例輸出說明:
BATC

因CDE{BATC}中，為最短且都有ABC的情況，
所以輸出為BATC，雖然CDEBA也滿足，
但它不是最短的。

sample input:

CDEBATC
ABC

sample output:

BATC

-----------------------------------------
sample input2:

ABCBCAABABAC
ACCAB

sample output2:

CBCAA

note:題目不會有找不到或是有兩個同長度且滿足需求的情況!!!
'''
def test(str_all,str_B):
    str_all = list(str_all)
    str_B = list(str_B)
    for i in range(len(str_B)):
        if str_B[i] in str_all:
            str_all.remove(str_B[i])
        else:
            return False
    return True

def main():
    for i in range(len(str_A)-len(str_B)+1,0,-1):
        for j in range(i):
            str_all = str_A[j:j+len(str_A)-i+1]
            if test(str_all,str_B):
                print(str_all)
                return
str_A = input()
str_B = input()
main()