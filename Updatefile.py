import os
data = pd.read_csv('nasdaqtraded.csv')
tickers= data["Symbol"]
for i in tickers[:5]:
    if len(pd.read_csv('data\data'+i+'.csv'))>1:
        #print(i)
        datastock= pd.read_csv('data\data'+i+'.csv')
        lastdate= datastock["Date"].iloc[-1]
        print("iloc[-1] of existing file",lastdate, "current date" ,datecurrent)
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
            
            f=datastock.append(new.iloc[2:])
            f.to_csv('data\data'+i+'.csv', index=False)   
            print("true")
        else:
            pass
            print("false", newdate, " kleiner oder gleich als " , lastdate)
