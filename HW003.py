"""
數值運算:
分別輸入 num1 num2 求出兩數的 Sum,Difference,Product,Quotient。

結果須輸出到小數點第二位
print("%.2f" %x1);

輸入:
25
2

NOTE:Difference為相差，並非25-2，而是兩數之間的差

輸出:
Difference:23.00
Sum:27.00
Quotient:12.50
Product:50.00
"""
num1=input()
num2=input()
print('Difference:',end='')
print(format(abs(float(num1)-float(num2)),".2f"))   #abs()求絕對值
print('Sum:',end='')
print(format(float(num1)+float(num2),".2f"))        #float()定義為小數
print('Quotient:',end='')
print(format(float(num1)/float(num2),".2f"))
print('Product:',end='')
print(format(float(num1)*float(num2),".2f"))