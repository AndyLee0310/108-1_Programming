'''
039.未讀訊息
時下最流行的通訊軟體為Line，使用者會反覆登入看訊息，
程式會根據過去和當前訊息的時間戳，在已讀和未讀訊息中間
以一條明顯的分隔線做分隔，方便使用者快速略過已讀訊息，
讀取最新的訊息。
請你以程式模擬上述情形。

輸入說明:
先輸入一個整數n代表有n個訊息，接下來n行輸入由時間戳記t、訊息m所組成的資料，
例如:1516843860 Alan: hi, Terry，則1516843860為時間戳記，Alan: hi, Terry為訊息，
再輸入整數s，代表使用者讀取的時間戳記個數為s個，接下來s行輸入使用者讀取的時間戳記。
註:時間戳記後面一定比前面大

輸出說明:
根據使用者讀取的時間戳記，輸出未讀取的訊息記錄。請注意，已讀訊息與未讀訊息中間請以"-"符號隔開。

Sample Input
5
1516843860 Alan: hi, Terry
1516843980 Alan: I'm at ChengCheng stationery shop now
1516844040 Alan: what other materials are missing?
1516844160 Terry: yeah, we still lack 50 pastel papers
1516844220 Terry: could you get it back please?
4
1516843920
1516844100
1516844150
1516844340

Sample Output
Alan: hi, Terry
-
Alan: I'm at ChengCheng stationery shop now
Alan: what other materials are missing?
-
Terry: yeah, we still lack 50 pastel papers
Terry: could you get it back please?
'''
num=int(input())
times=[input().split() for i in range(num)]
for i in range(num):
    times[i][0]=int(times[i][0])
num2=int(input())
t1=[[int(input()),'-'] for i in range(num2)]
times=times+t1

times=sorted(times,key=lambda times: times[0])

if times[-1]=='-':
    for i in range(len(times)-1):
        if times[i][1]=='-'and times[i+1][1]=='-':
            pass
        else:
            if not(i==(len(times)-1) and times[i][1]=='-'):
                for x in range(1,len(times[i])):
                    print(times[i][x],end=' ')
            print()
else:
    for i in range(len(times)):
        if times[i][1]=='-'and times[i-1][1]=='-':
            pass
        else:
            if not(i==(len(times)-1) and times[i][1]=='-'):
                for x in range(1,len(times[i])):
                    print(times[i][x],end=' ')
            print()