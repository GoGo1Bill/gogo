import datetime
import time
import pyupbit
import requests

access = "qxIkB04AqH58X96HtJ5jlnadCqeX694RuY5YYlEr"
secret = "caK9Mwuw37xPazOX8unTNFzGlKKzDxg8Kxlh2Equ"

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2609205237909-2597943438071-vCgmFZLLkDC8qNUs0cGXVEkA"

def get_start_time1(KRWDOGE):
    df1= pyupbit.get_ohlcv("KRW-DOGE", interval="day", count=1)
    start_time1 = df1.index[0]
    return start_time1

def get_balance(KRWDOGE):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == KRWDOGE:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

    return 0

def get_current_price(KRWDOGE):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=KRWDOGE)["orderbook_units"][0]["ask_price"]
    
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
post_message(myToken,"#crypto", "autotrade start")

while True:
     try:
        now1 = datetime.datetime.now()
        start_time1 = get_start_time1("KRW-DOGE")
        end_time1 = start_time1 + datetime.timedelta(days=1)


        df3 = pyupbit.get_ohlcv("KRW-DOGE", interval="minute5", count=1)
        target1 = df3.iloc[0]['close'] - df3.iloc[0]['open']

        df5 = pyupbit.get_ohlcv("KRW-DOGE", interval="minute1", count=1)
        current1 = df5.iloc[0]['close']

        balances = upbit.get_balances()
        print (balances)

        if start_time1 < now1 < end_time1 - datetime.timedelta(seconds=10):
            if target1 >= 4 :
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-DOGE", krw*0.9995)
                    post_message(myToken,"#test", "buy : " + str(current1)+"/"+str(balances))
                    
        
            else :
               target1 <= -2
               doge = get_balance("DOGE")
               if doge > 20:
                   upbit.sell_market_order("KRW-DOGE", doge*0.9995)
                   post_message(myToken,"#crypto", "sell : " + str(current1)+"/"+str(balances))
            time.sleep(10)                
                          
     except Exception as e:
        print(e)
        post_message(myToken,"#crypto", e)
        time.sleep(10)