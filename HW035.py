'''
數字GCD大家都算過，那字串的呢？

字串GCD定義範例如下

GCD(ABCABC, ABC) = ABC

GCD(ABABAB, ABAB) = AB

GCD(AAAAAA, AAAAA) = A

你能幫忙求出字串的GCD嗎？

輸入說明:
每一行有兩個字串s1、s2
輸入皆為大寫英文字母
至-1結束

輸出說明:
輸出兩字串的GCD
如果兩字串沒有GCD，輸出"No GCD"

Sample Input
ABCABC ABC
ABABAB ABAB
AAAAAA AAAAA
ZERO JUDGE
-1

Sample Output
ABC
AB
A
No GCD
'''
def GCD(str_A,str_B):
    len_A, len_B = len(str_A), len(str_B)
    x = min(len_A,len_B)
    s=[]
    for i in range(1,x+1):
        if len_A % i or len_B % i:
            continue
        xA, xB = int(len_A/i), int(len_B/i)
        gcd = str_A[:i]
        sA = gcd * xA
        sB = gcd * xB
        if sA == str_A and sB == str_B:
            s.append(gcd)
    if len(s)!=0:
        return max(s)
    else:
        return ""
def main():
    a=[]
    while True:
        s=input().split(' ')
        if s[0]!='-1':
            x=GCD(s[0], s[1])
            if len(x)!=0:
                a.append(x)
            else:
                a.append('No GCD')
        else:
            break
    for x in a:
        print(x)     
main()