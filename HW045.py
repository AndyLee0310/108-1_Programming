'''
045
輸入兩個單字w1 and w2，
請計算出將w1變成w2最少需要多少次操作。

你可進行的操作包含以下
1.插入一個字元
2.刪除一個字元
3.替換一個字元

範例輸入:
horse
ros

範例輸出:
3

範例輸出說明:
替換操作 horse -> rorse(將h換成r)
刪除操作 rorse -> rose(將中間的r刪除)
刪除操作 rose-> ros(將e刪除)
'''
def test(x, y):
    if x == y:
        return 0
    if len(x) < len(y):
        x, y = y, x
    if not x:
        return len(y)
    previous_row = range(len(y) + 1)
    for i, column1 in enumerate(x):
        current_row = [i + 1]
        for j, column2 in enumerate(y):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (column1 != column2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1] 
x=input()
y=input()
print(int(test(x,y)))