import requests
import pandas
import time

def action(i):
    url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey=demo".format(i)
    r = requests.get(url)
    time.sleep(13)
    data = r.json()
    print(data)
    df = pandas.DataFrame([data])
    RequiredDF = df[["Symbol","Name","Country","Sector","Industry","Address"]]
    Temp.append(RequiredDF)
    
company =["BHG","CCRN","CHCT","CHNG","CLOV","DH","IBM","GOOGl","ABC","AAPL","BOXL","BRQS","CAJ","CAN","AFG","ALLY","ALRS","AMAL","AMBC","HAFC","ADM","AGRO","ALCO"]
Temp = []
for i in company:
    try:
        action(i)
        print("Success")
    except Exception as e:
        print(str(e),i)

Final = pandas.concat(Temp)
Final.to_csv("Stocks_Detail.csv",index=False)