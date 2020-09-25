"""
質因數分解

輸入一個整數，將該正整數表示成質因數乘積。

輸入說明：
輸入一正整數。

輸出說明：
將整數分解為質因數的積，由小列到大，兩質數之間以 * 符號連結。

Sample input：
90

Sample output：
2*3*3*5
"""
def get_num_factors(num):
    list0=[]
    tmp=2
    if num==tmp:
        print(num)
    else:
        while (num>=tmp):
            k=num%tmp
            if( k == 0):
                list0.append(str(tmp))
                num=num/tmp  #更新
            else:
                tmp=tmp+1  #同时更新除数值，不必每次都从头开始
        print('*'.join(list0))

num=int(input())
get_num_factors(num)