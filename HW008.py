"""
008.
輸入為一個英文句子加上一個單字，
請print出句子的長度，並且把句子中有出現的該單字移除，
範例輸入說明:
一個英文句子
一個英文句子中有出現的單字

範例輸出說明:
輸出句子的長度
輸出已被移除存在單字的句子

Sample Input:
Those who turn back never reach the summit.
who

Sample Output:
43
['Those ', ' turn back never reach the summit.']
"""

A=input()
word=input()

print(len(A))
newA=A.split(word)
print(newA)