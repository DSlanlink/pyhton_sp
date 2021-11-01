import pandas as pd

df_weather = pd.read_csv(r'D:\qixiangdashuju.csv',header=0,index_col=0)
# ['1'].str.contains('澳门')
# see = df_weather.loc[('澳门')]
df_weather.drop('历史最高气温',axis=1,inplace=True)
df_weather.drop('\t历史最低气温',axis=1,inplace=True)

new_rain = df_weather['平均降水量']

rain_list = []
for rain in new_rain:
    so_ain = rain.split('mm')[0]
    rain_list.append(so_ain)
df_weather['平均降水量'] = rain_list


def get_hight(been):
    hight_list = []
    for  i in been:
        hight_list.append(i[:-1])
    been = hight_list
    return been

df_weather['平均最高温度']=get_hight(df_weather['平均最高温度'])
df_weather['平均最低温度']=get_hight(df_weather['平均最低温度'])
df_weather['月份'] = get_hight(df_weather['月份'])
print(df_weather)
#
# df_weather.to_excel(r'D:\soso.xlsx',index=None)