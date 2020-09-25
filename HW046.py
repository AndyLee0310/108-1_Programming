'''
046
輸入一組數字，請將該數字對應以下表格進行編碼，
並且輸出他編碼後有幾種可能。

A -> 1
B -> 2
...
Z ->26

範例輸入:
12

範例輸出:
2

範例輸出說明:
12可以編碼為1:A, 2:B
也可以編碼為12:L
所以共2種

note:輸入不會超過20位
'''
def test(words, n):  
    count = [0] * (n + 1)  # A table to store  
                           # results of subproblems  
    count[0] = 1
    count[1] = 1
    for i in range(2, n + 1):  
        count[i] = 0
        # If the last digit is not 0, then last 
        # digit must add to the number of words  
        if (words[i - 1] > '0'):  
            count[i] = count[i - 1] 
        # If second last digit is smaller than 2 
        # and last digit is smaller than 7, then 
        # last two words form a valid character  
        if (words[i - 2] == '1' or 
           (words[i - 2] == '2' and 
            words[i - 1] < '7') ):  
            count[i] += count[i - 2]
    return count[n]
# Driver Code 
words =input() 
n = len(words)
print(test(words, n))