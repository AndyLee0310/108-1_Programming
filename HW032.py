"""
032. 數字穿插

給定一串數字，必須將該數字重新排序，
重新編排後，數字的左右兩側不能是自己，
且必須由小到大排序，
輸出的結果必須為最小的數字，
且符合左右兩側不能是自己的條件。

詳細說明:
假設給你一個1 2 2 3的數字，
左右不能是自己的條件狀況有，
1232 2132 2123 3212，
而輸出必須為其中最小數字，
所以答案是1232。

PS:題目不會有排不出來與Output超過int上限的情況
還有不會有兩位數以上的狀況如: 10 11 21(不過想挑戰的人可以試試看)


Input:
1 1 1 1 2 2 3 3

Output:
12121313

Input:
1 1 1 2 3 2 2 2 2

Output:
212121232
"""
import itertools
def test(b):
    w = True
    a = len(b)
    for i in range(1,a-1):
        if b[i] == b[i+1] or b[i] == b[i-1]:
            w = False
            break
    return w
nums = input().split()
x = list(set(itertools.permutations(nums)))
y = []
for i in range(len(x)):
    if test(x[i]):
        y.append(int(''.join(x[i])))
print(min(y))