from pyecharts.faker import Faker
import pandas as pd
from pyecharts.charts import Pie,Bar,Map,WordCloud,Page
from pyecharts import options as opts

df = pd.read_csv(r'E:\DATA\been.csv',encoding='utf-8')
# print(df['location'],df['mm'])
print(df)
def get_num():
    new_list = []
    for i,j in zip(df['地区'],df['年总降水量']):
        result = i,j
        new_list.append(result)

    return new_list



we =[]
for i in df['地区']:
    we.append(i)
print(we)

ye = []
for j in df['年总降水量']:
    ye.append(j)
print(ye)

bar = (
      Bar()
      .add_xaxis(we)
      .add_yaxis('降雨',ye)
      .set_global_opts(
          title_opts=opts.TitleOpts(title="一年的降水量与蒸发量"),
          datazoom_opts=opts.DataZoomOpts(),

      )
      .set_series_opts(
          label_opts=opts.LabelOpts(is_show=False),
  )
)
bar.render()