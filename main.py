import pandas as pd

df_pd = pd.read_csv(r'C:\Users\DSlanlink\Desktop\天气数据\数据集\气象.csv',encoding='gbk')

df_pd.drop_duplicates(inplace=True)

new_rain = df_pd['平均降雨量']

rain_list = []
for rain in new_rain:
    rain_list.append(rain.split('m')[0])

df_pd['平均降雨量'] = rain_list

def quchu(been):
    wendu_list = []
    for i in been:
        wendu_list.append(i[:-1])
    been = wendu_list
    return been
df_pd['平均最高气温'] = quchu(df_pd['平均最高气温'])

df_pd['平均最低气温'] = quchu(df_pd['平均最低气温'])

df_pd['月份'] = quchu(df_pd['月份'])

df_pd.drop("历史最高气温",axis=1,inplace=True)
df_pd.drop("历史最低气温",axis=1,inplace=True)

df_pd.to_excel(r'C:\Users\DSlanlink\Desktop\天气数据\数据集\qixiang.xlsx',index=None)
print(df_pd)