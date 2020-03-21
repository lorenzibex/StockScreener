import pandas as pd
import yfinance as yf
import os

#ONLY NON-ETF STOCKS AND DELETE LAST ROW
data = pd.read_csv('nasdaqtraded.csv')
data["Symbol"].equals(data["NASDAQ Symbol"])
onlyStockSym = []
dataetf = data['ETF']
dataSym = data['Symbol']

for i in range(len(data)): # DO NOT APPEND ETF SYMBOLS
    if  data['ETF'][i] == 'N': 
        onlyStockSym.append(data['Symbol'][i])       
tickers= data["Symbol"][:-1] # last element is NaN 
#print(tickers.tail(n=4), type(tickers))
#print(onlyStockSym[-1])

from datetime import datetime, timedelta

now =datetime.now()
print(now)

import csv

import time
N = 0.25
sixHours_ago = datetime.now() - timedelta(days=N)
print(datetime.now())
datecurrent=sixHours_ago.strftime("%Y-%m-%d")
print(datecurrent[0:10], len(datecurrent))

#type(date_N_days_ago)
#type("a")
#print('Current Timestamp : ', timestampStr)
type(datecurrent)
print( lastdate, datecurrent)



tickers= data["Symbol"]
for i in tickers:
    if len(pd.read_csv('quot\data'+i+'.csv'))>1:
        try:
            datastock= pd.read_csv('quot\data'+i+'.csv')
            lastdate= datastock["Date"].iloc[-1]
            print(i , "iloc[-1] of existing file",lastdate, "current date" ,datecurrent)
            yf.download(i, start =lastdate, end =datecurrent ).to_csv(str(lastdate)+'-'+str(datecurrent )+str(i)+'.csv')
            time.sleep(0.01) 
            new=pd.read_csv(str(lastdate)+'-'+str(datecurrent )+str(i)+'.csv')
            os.remove(str(lastdate)+'-'+str(datecurrent )+str(i)+'.csv')
            newdate =new["Date"].iloc[-1]
            firstdatedown = new["Date"].iloc[1]
            print(newdate, "download.iloc[-1 ", firstdatedown , "download.iloc[1 ")
        #print(i, new)
        #print(new.iloc[2], "new.iloc[2]")
    #print(datastock.iloc[-4:,:3], ' \n', "new",new,"newdate", newdate)
            if newdate > lastdate:
                try:
                    f=datastock.append(new.iloc[2:])
                    f.to_csv('quot\data'+i+'.csv', index=False)
                    print("true")
                except:
                    print("Except")
            else:
                pass
                print("false", newdate, " kleiner oder gleich als " , lastdate)
        except:
            pass
