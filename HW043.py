'''
043.Google搜尋器
讓我們來用程式模擬Google的搜尋器

輸入說明:
先輸入整數N，代表有N筆資訊(一串文字，包含特殊字元、空格...)，接著輸入N行
資訊，再輸入使用者要的關鍵字(一行以空格隔開的關鍵字詞)

輸出說明:
根據資訊中包含幾項關鍵字的多寡進行排序，由多到少印出(若一樣，則照字典印出)，並將匹配到的關鍵字全部大寫，其他保持原樣
(若拼字不完全相同，例如engineer、eng，則輸出ENGineer；大小寫不同仍視為相同，例如engINeer、NEER，則輸出engINEER)。
方便使用者找到自己想要的資料。

Sample Input:
5
National Taipei University of Technology, Taipei Tech
National Taiwan University of Science and Technology, Taiwan Tech
Department of Computer Science and Information Engineering, National Taiwan University of Science and Technology
Department of Computer Science and Information Engineering, Taipei Tech
Department of Computer Science and Information Engineering, National Taiwan University
Taipei Tech comPuTer Science engineer

Sample Output:
Department of COMPUTER SCIENCE and Information ENGINEERing, National Taiwan University of SCIENCE and TECHnology
Department of COMPUTER SCIENCE and Information ENGINEERing, TAIPEI TECH
National TAIPEI University of TECHnology, TAIPEI TECH
Department of COMPUTER SCIENCE and Information ENGINEERing, National Taiwan University
National Taiwan University of SCIENCE and TECHnology, Taiwan TECH
'''
num = int(input())
sx=[""]*num
spx=[[]]*num
c={}
for i in range(num):
    sx[i]=str(input())
    spx[i]=sx[i].split(" ")
    c.setdefault(i,0) 
a=[]
s = str(input())
sp = s.split(" ")
for string in sp:    #先從搜尋第一個字開始
    string = string.lower() #轉小寫
    for sxtring in range(len(sx)):#第幾行字串
        for spxlit in range(len(spx[sxtring])):#此字串被空白split
            spxlit2 = spx[sxtring][spxlit].lower()
            if(string in spxlit2):  #如果搜尋的字在被空白split裡
                c[sxtring]+=1
                spx[sxtring][spxlit] = (spxlit2.replace(string,string.upper()))#轉成大寫
            else:
                spx[sxtring][spxlit] = spx[sxtring][spxlit]#原本的格式輸出(防止前面轉小寫轉到)
for x in range(len(sx)):
    sx[x] = " ".join(spx[x])#合併split
for key,value in c.items():
    a.append([value,key])
a = sorted(a,reverse=True)
ok=False
for ik in range(len(a)-1):
    if(not ok):
        temp=[]
    if(a[ik][0] == a[ik+1][0]):
        temp.append(sx[a[ik][1]])
        ok=True
        continue
    elif(ok):
        temp.append(sx[a[ik][1]])
        temp.sort()
        for k in range(len(temp)):
            sx[a[ik-(len(temp)-k-1)][1]]=temp[k]
        ok=False
if(ok):
    temp.append(sx[a[ik+1][1]])
    temp.sort()
    for k in range(len(temp)):
        sx[a[ik+1-(len(temp)-k-1)][1]]=temp[k]
    ok=False
for i in a:
    print(sx[i[1]])