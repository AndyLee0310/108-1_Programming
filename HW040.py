"""
摩斯密碼
請使用Dictionary製作摩斯密碼對應表(使用"."和"-")，
把文字加密為摩斯密碼後分行輸出。

摩斯密碼對應表:https://zh.wikipedia.org/wiki/%E6%91%A9%E5%B0%94%E6%96%AF%E7%94%B5%E7%A0%81

輸入說明:
輸入一行欲加密的英數字。
註:只會有大寫英文字、數字不會有空格、其他字元

輸出說明:
將英數字加密後分行印出。
註:不用空格隔開!

Sample Input:
ABCD0

Sample Output:
.-
-...
-.-.
-..
-----
"""
morse_code={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
'F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-',
'L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-',
'R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--',
'X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---',
'3':'...--','4':'....-','5':'.....','6':'-....','7':'--...',
'8':'---..','9':'----.','0':'-----'
}

word = input()
for i in range(0,len(word)+1,1):
    print(morse_code[word[i]])