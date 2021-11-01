#coding:UTF-8
import time
import requests
import json
import csv
dt = "2014-09-17 20:00:00"
dt2 = "2021-07-12 20:00:00"

#转换成时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
timeArray2 = time.strptime(dt2, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
timestamp = time.mktime(timeArray)
timestamp2 = time.mktime(timeArray2)

time_start = int(timestamp)
time_out = int(timestamp2)
url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1410955200&timeEnd=1626091200"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
}

response = requests.get(url,headers = header)
new_response = json.loads(response.text)

beens = new_response['data']['quotes']
for i in beens:
    new_time = i['timeOpen'].split('T')[0]
    new_open = i['quote']['open']
    high = i['quote']['high']
    low = i['quote']['low']
    close = i['quote']['close']
    volume = i['quote']['volume']
    markecap = i['quote']['marketCap']
    result = str(new_time),str(new_open),str(high),str(low),str(close),str(volume),str(markecap)
    print(result)
    try:
        with open('D:\\Bitcoin.csv', 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(result)

    except IndexError:
        continue
