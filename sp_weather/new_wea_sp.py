import pandas as pd

from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
from pyecharts.charts import Pie, Bar, Map, WordCloud, Page
from pyecharts.faker import Faker
from pyecharts.charts import Line

df = pd.read_csv(r'E:\DATA\supershabi.csv', encoding='gbk')

nf = pd.read_csv(r'E:\DATA\super.csv', encoding='gbk')


def get_num():
    new_list = []
    for i, j in zip(df['city'], df['year_rain']):
        result = i, j
        new_list.append(result)

    return new_list


map = (
    Map()
        .add('降雨量',
             [list(lo) for lo in get_num()], 'china-cities',
             label_opts=opts.LabelOpts(is_show=False),
             is_map_symbol_show=False
             )
        .set_global_opts(
        title_opts=opts.TitleOpts(title='全国历年平均总降水量 单位（mm）'),
        visualmap_opts=opts.VisualMapOpts(max_=3000, is_piecewise=True),

    )
)

we = []
for i in nf['city']:
    we.append(i)

ye = []
for j in nf['year_temp']:
    ye.append(j)

bar = (
    Bar()

        .add_xaxis(we)
        .add_yaxis('平均温度', ye)
        .set_global_opts(

        title_opts=opts.TitleOpts(title="江苏省城市历年平均气温 单位（℃）"),
        datazoom_opts=opts.DataZoomOpts(),

    )
        .set_series_opts(
        label_opts=opts.LabelOpts(position="right")
        # label_opts=opts.LabelOpts(is_show=False),
    )
        .reversal_axis()
)
new_we = []
for i in nf['code_wind']:
    new_we.append(i)

new_city = []
for j in nf['city']:
    new_city.append(j)

c = (
    Line()
        .add_xaxis(new_city)
        .add_yaxis('江苏城市静风发生概率 单位（%）', new_we)

)


def get_pie():
    pie_list = []
    for i, j in zip(nf['city'], nf['can_see']):
        result = i, j
        pie_list.append(result)

    return pie_list


pie = (
    Pie()

        .add(
        "",
        [list(z) for z in get_pie()],
        radius=["30%", "75%"],
        center=["50%", "50%"],
        rosetype="area",
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="能见度 单位（千米）",
                                                   pos_left="center"),
        legend_opts=opts.LegendOpts(is_show=False)
                         )
        .set_series_opts(legend_opts=opts.LegendOpts(is_show=False), tooltip_opts=None)

)

page = Page(layout=Page.DraggablePageLayout)
page.add(map, bar, c, pie)
page.render()

Page.save_resize_html('render.html',cfg_file= 'chart_config (7).json')
