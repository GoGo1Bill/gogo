import datetime
import time
import pyupbit
import requests

access = "access"
secret = "secret"

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "secret"

def get_start_time1(KRWDOGE):
    df1= pyupbit.get_ohlcv("KRW-BORA", interval="day", count=1)
    start_time1 = df1.index[0]
    return start_time1

def get_balance(KRWDOGE):

    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == KRWDOGE:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

    return 0

def get_current_price(KRWDOGE):
    
    return pyupbit.get_orderbook(ticker=KRWDOGE)["orderbook_units"][0]["ask_price"]
    
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
post_message(myToken,"#test", "autotrade start")

while True:
     try:
        now1 = datetime.datetime.now()
        start_time1 = get_start_time1("KRW-DOGE")
        end_time1 = start_time1 + datetime.timedelta(days=1)


        df3 = pyupbit.get_ohlcv("KRW-DOGE", interval="minute5", count=1)
        target1 = df3.iloc[0]['close'] - df3.iloc[0]['open']
        volume = df3.iloc[0]['volume']
        print (target1)

        df5 = pyupbit.get_ohlcv("KRW-DOGE", interval="minute1", count=1)
        current1 = df5.iloc[0]['close']

        balances = upbit.get_balances()
        print (balances)

        if start_time1 < now1 < end_time1 :
            if target1 >= 3 and volume >= 10000000 :
                krw = get_balance("KRW")
                if  krw > 5000:
                     upbit.buy_market_order("KRW-DOGE", krw*0.01)
                     post_message(myToken,"#test", "buy : " + str(current1)+"/"+str(krw))
                    
        
            if target1 <= -3 and volume >= 10000000 :
                doge = get_balance("DOGE")
                if doge > 0:
                    upbit.sell_market_order("KRW-DOGE", doge*0.001)
                    post_message(myToken,"#test", "sell : " + str(current1)+"/"+str(krw))
            time.sleep(299.5)     

                          
     except Exception as e:
        print(e)
        post_message(myToken,"#test", e)
        time.sleep(300)