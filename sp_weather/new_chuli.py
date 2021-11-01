import pandas as pd

df = pd.read_csv(r'E:\DATA\name (2).csv',encoding='gbk')

ci_list = []
for ci in df['城市名称']:
    if '市' in ci:
        new_ci = ci.replace('市','')
        ci = new_ci
    ci_list.append(ci)

df['城市名称'] = ci_list

sp_list=[]
for sp in df['城市名称']:
    if '地区' in sp:
        new_sp = sp.replace('地区','')
        sp = new_sp
    sp_list.append(sp)

df = df.astype(str)#类型强制转换
y = df[df['城市名称'].str.contains('/')]#包含‘/‘字符串的列表

test1 = list(y.城市名称)
test2 = list(df.城市名称)
#选取两个不同的列表，然后通过set的方法对列表相同的字符串进行删减，并且产生新的列表
ret = list(set(test2) ^ set(test1))
result = df[df.城市名称.isin(ret)]
#isin，在原来的列中选取，ret列表中所含有的数据

ss = result.isna()
result.dropna(axis=0, how='any')


df.to_csv(r'E:\DATA\supershabi.csv',encoding='gbk')