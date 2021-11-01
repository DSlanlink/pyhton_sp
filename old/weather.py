import requests
import json
from lxml import etree
import csv

url = 'http://www.tianqihoubao.com/lishi/nanjing/month/202001.html'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Referer': 'http://www.tianqihoubao.com/'
}

response = requests.get(url, headers=header,timeout=5)
html = response.text
been = etree.HTML(html)

citys = been.xpath('//*[@class="box pcity"]//ul/li/a/@href')
newcity_list = []
for city in citys:
    new_city = city[7:].split('.')[0]
    newcity_list.append(new_city)
    nub_list = ['01','02','03','04','05','06','07','08','09','10','11','12']
    urls = ['http://www.tianqihoubao.com/lishi/{}/month/2020{}.html'.format(j,i) for i in nub_list for j in newcity_list]
    for url in urls:
        response = requests.get(url,headers = header )
        response.encoding='utf-8-sig'
        html = response.text

        been = etree.HTML(html)

        date = been.xpath('//*[@id="content"]/table/tr/td[1]/a/@title')
        name = been.xpath('//*[@id="content"]/table/tr/td[2]/text()')
        numbers = been.xpath('//*[@id="content"]/table/tr/td[3]/text()')
        fox = been.xpath('//*[@id="content"]/table/tr/td[4]/text()')
        for i , j ,g ,y  in zip(name,date,numbers,fox):
            name1 = j.replace('\n', '').replace('\r', '').replace(' ',''),
            name2 = i.replace('\n', '').replace('\r', '').replace(' ',''),
            name3 = g.replace('\n', '').replace('\r', '').replace(' ',''),
            name4 = y.replace('\n', '').replace('\r', '').replace(' ','')
            result = name1,name2,name3,name4
            print(type(result))
            try:
                with open('D:\\nanjing.csv', 'a', newline='',encoding='utf-8-sig') as f:
                    w = csv.writer(f)
                    w.writerow(result)

            except IndexError:
                continue