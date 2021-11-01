import requests
from lxml import etree
import urllib3
import csv

urllib3.disable_warnings()

def noteurl():
    url1 = [
        'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&pvid=f2eaac2a8bb0490580626043ba2f00ad&page={}&s=117&click=0'.format(m) for m in range(1, 100, 2)]
    return url1

def superurl():
    new_id = []
    for new_url in noteurl():
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'Connection': 'close'
        }
        response = requests.get(new_url, headers=header, verify=False)
        response_text = response.text
        # //*[@id="J_goodsList"]/ul/li/@data-sku
        html = etree.HTML(response_text)
        number_id = html.xpath('//*[@id="J_goodsList"]/ul/li/@data-sku')
        new_id.append(number_id)
    return new_id
ss = []
for super_id in superurl():
    for m in super_id:
        ss.append(m)
        url2 = ['https://item.jd.com/{}.html'.format(j) for j in ss]

        def number_request():
            been = []
            for name in url2:
                been.append(name)

            return been
def jiexi():
    gg = []
    for newsuper_url in number_request():
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'Connection': 'close',
            'Cookie': '__jdu=226194557; areaId=12; shshshfpa=efa5f2bb-78e7-8011-c7b6-7b0912bb2b86-1624110866; shshshfpb=wCfNTa%20AmNuVm1VNbf21LOA%3D%3D; ipLoc-djd=12-978-980-36485; pinId=tu1pCJf8uvdKnDbQpYNWbQ; pin=jd_dGVkbFsdIvjA; unick=%E6%B2%A1%E6%9C%89%E4%BD%A0%E7%9A%84%E6%99%AE%E5%AE%89; _tp=QASLLIDWLBplsgHdi8TgtQ%3D%3D; _pst=jd_dGVkbFsdIvjA; dsp_max=845a65f873acb3f.rdARr9EeqtEZrdMZrtcarNwYq9UYr9Q; unpl=V2_ZzNtbUtfFkB1ChIALxlcBGJTR1pKUUdGdQhEUykfW1U3AxIKclRCFnUUR1NnGlwUZgoZWEZcQxdFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHgaWwVvBhZZRGdzEkU4dlxyGFkMYTMTbUNnAUEpC0Ncex9dSGQAFV1KUkcRczhHZHg%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_89dd13eee1104ad6975b1136c76aa11f|1624236310763; PCSYCityID=CN_320000_320400_0; __jda=122270672.226194557.1624110861.1624193867.1624236311.4; __jdc=122270672; shshshfp=cc0f1c0f5f8be26db83f5e1804ebeb76; wlfstk_smdl=kjj6xzr6jwcadmivmb6hbcyzq6w6tz8d; TrackID=1pbIYejtGQYAqOVFezbX-4ExNqgV45V0AJj-LLyavxYXA0Ax8G9rYOkW3H806B13h4N45rM4pUdTzYD--2EjbrPFMXbyb1o2ZHT272Lg7_0s; ceshi3.com=103; 3AB9D23F7A4B3C9B=CKMJY2WCAYTIWDXPAXI3TIEQILCYIIQ3ZW5DJ3ISPT43FUDDKI6TIXJ4XFYYAKSFJ55J4LGKLE74KFHH47CPBFYZGY; shshshsID=14be499dad69a45818e9cbd6b74df8a1_5_1624236898594; __jdb=122270672.7.226194557|4.1624236311; thor=95196AF8D8A8F0C50A6DA5088311D7809A2BFB84DD1A62B953EC9A6DD7EDD7DEB326E89DDADDAA26F015F5F83CF85BB33EA676FA93FC011BAA5924659C09E8C1EDA7D950F8B34F129A80906079ACBC8955310974EB4ECF85448E755B11C3B8D651AB0A655F8FFA97BC9A56D66003F443AE6303097F51C2D38F407BCD5225FE724B69D5F3443702CDC8F8A5CE68369FA8EA0082B05A5FF94FDBA8C07E9334DC3D'

        }
        new_response = requests.get(newsuper_url, headers=header)
        manage = new_response.text
        html = etree.HTML(manage)

        name = html.xpath('//*[@id="parameter-brand"]/li/@title')

        new_name = name[0]
        #//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li/text()
        shop_name = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[1]/text()')
        wight_name = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[3]/text()')
        see_name = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[4]/text()')

        big_name = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[6]/text()')
        yingpan_name = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[7]/text()')
        chuliqi_name = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[8]/text()')
        xianka_name = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[9]/text()')
        # a = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[10]/text()')
        # b = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[11]/text()')
        # c = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[12]/text()')
        # d = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[13]/text()')
        # e = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[14]/text()')
        # f = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[15]/text()')
        # g = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[16]/text()')
        # h = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[17]/text()')
        # i = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[18]/text()')
        # j = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[19]/text()')
        # k = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[20]/text()')
        # L = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[21]/text()')
        # m = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[22]/text()')
        # n = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[23]/text()')
        # o = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[24]/text()')
        # p = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[25]/text()')


        mansuper = name[0], shop_name[0], wight_name, big_name, yingpan_name, chuliqi_name,xianka_name, see_name, a, b, c, d, e, f, i, g,h, j, k, L, m, n, o, p,  h
        print(mansuper)
        try:
            with open('D:\\been.csv', 'a', newline='') as f:
                w = csv.writer(f)
                w.writerow(mansuper)

        except IndexError:
            continue
if __name__ == '__main__':
    jiexi()