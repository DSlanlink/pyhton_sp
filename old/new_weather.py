import json
import requests
import csv

def urls():
    url = ['http://d1.weather.com.cn/calendar_new/2021/101020100_20210{}.html?_=1625048145511'.format(i) for i in range(1,7)]
    return url

def requesst_url():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Cookie': 'f_city=%E5%8C%97%E4%BA%AC%7C101010100%7C; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1625015725,1625016435,1625016658,1625047948; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1625048866',
        'Referer': 'http://www.weather.com.cn/'

    }
    ss = []
    for url in urls():

        response = requests.get(url,headers=header)
        response.encoding = 'utf-8'
        new_html = response.text
        datas  = json.loads(new_html[11:])
        ss.append(datas)
    return ss

def jiexi():
    for data in requesst_url():
        for new_datas in data:
            data = new_datas['date']
            higth = new_datas['hmax']
            low = new_datas['hmin']
            mansuper = data,higth,low
            try:
                with open('D:\\weather2.csv', 'a', newline='') as f:
                    w = csv.writer(f)
                    w.writerow(mansuper)

            except IndexError:
                continue

if __name__ == '__main__':
    jiexi()