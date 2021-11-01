import requests
from lxml import etree
import csv
url = ['https://www.ttpai.cn/quanguo/list-p{}'.format(i) for i in range(0,50)]
for su in url:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'cookie': 'ud=393752ee-f134-640d-1366-5e194ecfb866; utmSource=%7B%22utmSource%22%3A%22%22%2C%22utmMedium%22%3A%22SEO_www.baidu.com%22%2C%22utmCampaign%22%3A%22%22%2C%22utmContent%22%3A%22%22%2C%22utmTerm%22%3A%22%22%2C%22pageUri%22%3A%22https%3A%2F%2Fwww.ttpai.cn%2Fpaihangbang%2Fcx%22%2C%22bd_vid%22%3Anull%7D; ttpuid=U10a04a97-e134-640d-1366-601ee14acce8; Hm_lvt_dfe72aa58222e7b99f7951977db402e1=1626093264; _ga=GA1.2.2144502171.1626093264; _gid=GA1.2.1079904199.1626093264; ttpaiName=%E7%94%A8%E6%88%B7; tok=89e1aa256b847db0ba85d0efe3838b44; u=1335617; m=9H17s64X8KlxTSBv7TF0HQ%3D%3D; t=187****3057; Hm_lpvt_dfe72aa58222e7b99f7951977db402e1=1626093678'
    }
    response = requests.get(su,headers=headers)
    response.encoding='utf-8'
    # print(text)
    #数据解析成html对象
    html = etree.HTML(response.text)

    #/html/body/div[2]/div[3]/ul[1]/li/a/p[3]/strong/text()
    name = html.xpath('/html/body/div[2]/div[3]/ul[1]/li/a/h3/text()')
    price = html.xpath('/html/body/div[2]/div[3]/ul[1]/li/a/p[3]/strong/text()')
    for i ,j in zip(name,price):
        result = i,j
        try:
            with open('D:\\car.csv', 'a', newline='') as f:
                w = csv.writer(f)
                w.writerow(result)

        except IndexError:
            continue