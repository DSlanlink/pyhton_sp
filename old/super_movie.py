import requests

import urllib3
import csv
import json

urllib3.disable_warnings()

class supermovie(object):
    def __init__(self):
        self.header =  {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'Cookie': 'bid=1QO9bAu-PZU; douban-fav-remind=1; __gads=ID=506df243618ae45e-22769b0f06ca0014:T=1624762315:RT=1624762315:S=ALNI_MZV50jK29jJ8LjN4oDyPk6BBGNZEA; __utmz=30149280.1624762316.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="118163"; __utma=30149280.1984582479.1624762316.1624762316.1625964146.2; __utmc=30149280; __utmb=30149280.1.10.1625964146; __utma=223695111.513727893.1625964155.1625964155.1625964155.1; __utmb=223695111.0.10.1625964155; __utmc=223695111; __utmz=223695111.1625964155.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1625964155%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; _vwo_uuid_v2=DF04DED23EFE9CD35D75DBC728B19765A|260f4a1373213b4a9541ecae6ccffe67; _pk_id.100001.4cf6=8b6b510479abb047.1625964155.1.1625964879.1625964155.',
            'Referer': 'https://movie.douban.com/explore',
            'page_limit': '80'
                                }

    def urls(self,number):
        url = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit={}&page_start=0'.format(i) for i in range(0,number,20)]
        return url

    def requests_url(self):
        new_list = []
        for url in self.urls(number=1000):
            response = requests.get(url, headers=self.header, verify=False)
            name = response.text
            new_json = json.loads(name)
            new_been = new_json['subjects']
        print(new_list.append(new_been))
        new_list.append(new_been)
        return new_list

if __name__ == '__main__':
    supermovie().requests_url()