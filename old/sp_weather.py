import requests
from lxml import etree
import random
import csv
import json

header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
    'cookie':'Hm_lvt_2e69b379c7dbfdda15f852ee2e7139dc=1628409007,1628414519; Hm_lpvt_2e69b379c7dbfdda15f852ee2e7139dc=1628415009',
    'Referer': 'https://ii.911cha.com/blue/style.css?201905052'
}
def get_url():
    url ='https://tianqi.911cha.com/xuzhou/2020.html'
    response = requests.get(url,headers=header)
    response.encoding='utf-8'
    new_response = response.text

    been = etree.HTML(new_response)
    sp_urls = been.xpath('//*[@id="rmp1"]/li/a/@href')
    url_list = []
    for urls_sp in sp_urls:
        new_url_sp = urls_sp+'2020.html'
        url_list.append(new_url_sp)
    return url_list


print(get_url())
sp_weather_list =['https://tianqi.911cha.com/beijing/2020.html', 'https://tianqi.911cha.com/shanghai/2020.html', 'https://tianqi.911cha.com/xianggang/2020.html', 'https://tianqi.911cha.com/guangzhou/2020.html', 'https://tianqi.911cha.com/shenzhen/2020.html', 'https://tianqi.911cha.com/taibei/2020.html', 'https://tianqi.911cha.com/aomen/2020.html', 'https://tianqi.911cha.com/tianjin/2020.html', 'https://tianqi.911cha.com/shenyang/2020.html', 'https://tianqi.911cha.com/dalian/2020.html', 'https://tianqi.911cha.com/nanjing/2020.html', 'https://tianqi.911cha.com/suzhou/2020.html', 'https://tianqi.911cha.com/hangzhou/2020.html', 'https://tianqi.911cha.com/wuhan/2020.html', 'https://tianqi.911cha.com/chongqing/2020.html', 'https://tianqi.911cha.com/chengdu/2020.html', 'https://tianqi.911cha.com/wuxi/2020.html', 'https://tianqi.911cha.com/ningbo/2020.html', 'https://tianqi.911cha.com/hefei/2020.html', 'https://tianqi.911cha.com/xiamen/2020.html', 'https://tianqi.911cha.com/jinan/2020.html', 'https://tianqi.911cha.com/qingdao/2020.html', 'https://tianqi.911cha.com/zhengzhou/2020.html', 'https://tianqi.911cha.com/changsha/2020.html', 'https://tianqi.911cha.com/dongguan/2020.html', 'https://tianqi.911cha.com/xianshi/2020.html', 'https://tianqi.911cha.com/gaoxiong/2020.html', 'https://tianqi.911cha.com/shijiazhuang/2020.html', 'https://tianqi.911cha.com/tangshan/2020.html', 'https://tianqi.911cha.com/taiyuan/2020.html', 'https://tianqi.911cha.com/huhehaote/2020.html', 'https://tianqi.911cha.com/changchun/2020.html', 'https://tianqi.911cha.com/jilinshi/2020.html', 'https://tianqi.911cha.com/haerbin/2020.html', 'https://tianqi.911cha.com/xuzhou/2020.html', 'https://tianqi.911cha.com/changzhou/2020.html', 'https://tianqi.911cha.com/nantong/2020.html', 'https://tianqi.911cha.com/wenzhou/2020.html', 'https://tianqi.911cha.com/jiaxing/2020.html', 'https://tianqi.911cha.com/shaoxing/2020.html', 'https://tianqi.911cha.com/jinhua/2020.html', 'https://tianqi.911cha.com/fuzhou/2020.html', 'https://tianqi.911cha.com/quanzhou/2020.html', 'https://tianqi.911cha.com/nanchang/2020.html', 'https://tianqi.911cha.com/yantai/2020.html', 'https://tianqi.911cha.com/weifang/2020.html', 'https://tianqi.911cha.com/luoyang/2020.html', 'https://tianqi.911cha.com/xiangyang/2020.html', 'https://tianqi.911cha.com/zhuhai/2020.html', 'https://tianqi.911cha.com/shantou/2020.html', 'https://tianqi.911cha.com/foshan/2020.html', 'https://tianqi.911cha.com/zhongshan/2020.html', 'https://tianqi.911cha.com/nanning/2020.html', 'https://tianqi.911cha.com/haikou/2020.html', 'https://tianqi.911cha.com/guiyang/2020.html', 'https://tianqi.911cha.com/kunming/2020.html', 'https://tianqi.911cha.com/lanzhou/2020.html', 'https://tianqi.911cha.com/wulumuqi/2020.html', 'https://tianqi.911cha.com/zhangjiakou/2020.html', 'https://tianqi.911cha.com/yangquan/2020.html', 'https://tianqi.911cha.com/jincheng/2020.html', 'https://tianqi.911cha.com/shuozhou/2020.html', 'https://tianqi.911cha.com/yuncheng/2020.html', 'https://tianqi.911cha.com/linfen/2020.html', 'https://tianqi.911cha.com/wuhai/2020.html', 'https://tianqi.911cha.com/chifeng/2020.html', 'https://tianqi.911cha.com/tongliao/2020.html', 'https://tianqi.911cha.com/huludao/2020.html', 'https://tianqi.911cha.com/yanbian/2020.html', 'https://tianqi.911cha.com/yanji/2020.html', 'https://tianqi.911cha.com/mudanjiang/2020.html', 'https://tianqi.911cha.com/taicang/2020.html', 'https://tianqi.911cha.com/zhenjiang/2020.html', 'https://tianqi.911cha.com/suqian/2020.html', 'https://tianqi.911cha.com/yuyao/2020.html', 'https://tianqi.911cha.com/haining/2020.html', 'https://tianqi.911cha.com/tongxiang/2020.html', 'https://tianqi.911cha.com/shangyu/2020.html', 'https://tianqi.911cha.com/zhuji/2020.html', 'https://tianqi.911cha.com/taizhoushi/2020.html', 'https://tianqi.911cha.com/lishui/2020.html', 'https://tianqi.911cha.com/huangshan/2020.html', 'https://tianqi.911cha.com/chuzhou/2020.html', 'https://tianqi.911cha.com/fuyang/2020.html', 'https://tianqi.911cha.com/changle/2020.html', 'https://tianqi.911cha.com/putian/2020.html', 'https://tianqi.911cha.com/sanming/2020.html', 'https://tianqi.911cha.com/shishi/2020.html', 'https://tianqi.911cha.com/nanping/2020.html', 'https://tianqi.911cha.com/ningde/2020.html', 'https://tianqi.911cha.com/jingdezhen/2020.html', 'https://tianqi.911cha.com/shangrao/2020.html', 'https://tianqi.911cha.com/zaozhuang/2020.html', 'https://tianqi.911cha.com/tengzhou/2020.html', 'https://tianqi.911cha.com/dezhou/2020.html', 'https://tianqi.911cha.com/jiaozuo/2020.html', 'https://tianqi.911cha.com/huangshi/2020.html', 'https://tianqi.911cha.com/jingmen/2020.html', 'https://tianqi.911cha.com/xiaogan/2020.html', 'https://tianqi.911cha.com/shaoyang/2020.html']
#/html/body/div[2]/div[1]/div[1]/div[10]/table/tbody/tr[4]/td[1]/text()
for i in sp_weather_list:
    ne_response = requests.get(i,headers=header)
    ne_response.encoding='utf-8'
    been = etree.HTML(ne_response.text)
    rain=been.xpath('/html/body/div[2]/div[1]/div[1]/div[10]/table/tr[4]/td[1]/text()')
    city = been.xpath('/html/body/div[2]/div[1]/div[1]/div[2]/h2/text()')
    feng = been.xpath('/html/body/div[2]/div[1]/div[1]/div[12]/table/tr[3]/td[1]/text()')
    yun =been.xpath('/html/body/div[2]/div[1]/div[1]/div[16]/table[1]/tr[2]/td[1]/text()')
    wendu = been.xpath('/html/body/div[2]/div[1]/div[1]/div[16]/table[2]/tr[3]/td[1]/text()')
    result = city,rain,wendu,yun,feng
    print(result)
    try:
        with open('E:\\DATA\\soso.csv', 'a', newline='', encoding='gb18030') as f:
            w = csv.writer(f)
            w.writerow(result)

    except IndexError:
        continue

    print(result)