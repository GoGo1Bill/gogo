import datetime
import time
import pyupbit
import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2609205237909-2597943438071-CIarCJWwHPPGAGmCzkYqo5s6"

def get_start_time1(KRWDOGE):
    df1= pyupbit.get_ohlcv("KRW-DOGE", interval="day", count=1)
    start_time1 = df1.index[0]
    return start_time1

def get_start_time2(KRWAXS):
    df2 = pyupbit.get_ohlcv("KRW-AXS", interval="day", count=1)
    start_time2 = df2.index[0]
    return start_time2   

while True:
     try:
        now1 = datetime.datetime.now()
        start_time1 = get_start_time1("KRW-DOGE")
        end_time1 = start_time1 + datetime.timedelta(days=1)

        now2 = datetime.datetime.now()
        start_time2 = get_start_time2("KRW-AXS")
        end_time2 = start_time2 + datetime.timedelta(days=1)

        df3 = pyupbit.get_ohlcv("KRW-DOGE", interval="minute5", count=3)
        target1 = df3.iloc[-2]['close'] - df3.iloc[0]['open']

        df4 = pyupbit.get_ohlcv("KRW-AXS", interval="minute15", count=3)
        target2 = df4.iloc[-2]['close'] - df4.iloc[0]['open']
        volume2 = df4.iloc[2]['volume']
        
        df5 = pyupbit.get_ohlcv("KRW-DOGE", interval="minute1", count=1)
        current1 = df5.iloc[0]['close']

        df6 = pyupbit.get_ohlcv("KRW-AXS", interval="minute1", count=1)
        current2 = df6.iloc[0]['close']

        if start_time1 < now1 < end_time1 and start_time2 < now2 < end_time2:
            if target1 >= 3 or target1 <= -3 or target2 >= 1800 or target2 <= -1800 and volume2 >= 20000:

                 post_message(myToken,"#test", "price : " + str(current1) + "/" + str(current2))
                 print(current1)
                 print(current2)
                 time.sleep(30)
        
            else :
                 keep = -3 < target1 < 3 or -1800 < target2 < 1800 and volume2 < 20000
                 print(keep)
                 print(target1)
                 print(target2)
                 print(current1)
                 print(current2)
                 print(volume2)
                 time.sleep(30)
                 
                          
     except Exception as e:
        print(e)
        time.sleep(30)