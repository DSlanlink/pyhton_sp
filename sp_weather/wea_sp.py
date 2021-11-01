import requests
import json
import random
import csv
import time


requests.adapters.DEFAULT_RETRIES = 5

header = random.choice([{
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"},
    {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'},
    {
        "User-Agent": 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50'},
    {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'},
    {
        "User-Agent": 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'},
    {
        "User-Agent": 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)'}])


url = 'http://hz.hjhj-e.com/api/areas'
response = requests.get(url=url, headers=header)
new_response = json.loads(response.text)
been = new_response['data']
for id in been:
    sp_id = id['areaCode']
    sp_city = id['areaName']
    print(sp_id)
    new_url = 'http://hz.hjhj-e.com//api/cityEncycylopediaList?id=' + sp_id
    sp_resp = requests.get(url=new_url, headers=header)
    print(json.loads(sp_resp.text))
    try:
        new_sp_resp = json.loads(sp_resp.text)
        been = new_sp_resp['data']
        year_trmp = been['averageTemp']
        year_rain = been['monthRainfall']
        year_can_see = been['averageVis']
        code_wind = been['calmWind']
        result = sp_city, year_rain, year_trmp, year_can_see, code_wind
        print(result)

        with open('E:\\DATA\\55555.csv', 'a', newline='', encoding='gb18030') as f:
            w = csv.writer(f)
            w.writerow(result)

    except KeyError:
        continue
