import requests
from lxml import etree
import csv

def get_url():
    url = 'http://www.tianqihoubao.com/lishi/wuxi/month/202107.html'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    response = requests.get(url,headers = header)
    new_response = response.text

    been = etree.HTML(new_response)

    new_url = been.xpath('//*[@id="content"]/div[4]/a/@href')

    #http://www.tianqihoubao.com/
    li = []
    for i in new_url:
        new_i = 'http://www.tianqihoubao.com/'+i
        li.append(new_i)

    return li

def get_manage():
    for i in get_url():
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        response = requests.get(i,headers =header)
        new_response = response.text
        been = etree.HTML(new_response)

        date = been.xpath('//*[@id="content"]/table/tr/td[1]/a/@title')
        name = been.xpath('//*[@id="content"]/table/tr/td[2]/text()')
        numbers = been.xpath('//*[@id="content"]/table/tr/td[3]/text()')
        fox = been.xpath('//*[@id="content"]/table/tr/td[4]/text()')
        for i, j, g, y in zip(name, date, numbers, fox):
            name1 = j.replace('\n', '').replace('\r', '').replace(' ', ''),
            name2 = i.replace('\n', '').replace('\r', '').replace(' ', ''),
            name3 = g.replace('\n', '').replace('\r', '').replace(' ', ''),
            name4 = y.replace('\n', '').replace('\r', '').replace(' ', '')
            result = name1, name2, name3, name4
            print(result)

            try:
                with open('D:\\wuxi.csv', 'a', newline='',encoding='utf-8-sig') as f:
                    w = csv.writer(f)
                    w.writerow(result)

            except IndexError:
                continue


get_manage()