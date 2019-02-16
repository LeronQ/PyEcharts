
# coding: utf-8

# # 最基本的柱形图

# In[58]:


from pyecharts import Bar

bar1 = Bar("我的第一个图表", "这里是副标题")
# bar1.use_theme('dark') # 添加主题
bar1.add("服装",    # 纵坐标标注
        ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90],  #  横坐标属性，以及对应的Y值
        is_more_utils=True)  # 设置is_more_utils=True，是为了提供更多实用工具按钮
# bar1.render()   # 生成一个html的网页


# # 多次显示图表

# In[59]:


from pyecharts import Bar, Line
from pyecharts.engine import create_default_environment

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

line = Line("我的第一个图表", "这里是副标题")
line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

env = create_default_environment("html")
# 为渲染创建一个默认配置环境
# create_default_environment(filet_ype)
# file_type: 'html', 'svg', 'png', 'jpeg', 'gif' or 'pdf'

env.render_chart_to_file(bar, path='bar.html')
env.render_chart_to_file(line, path='line.html')


# 相比第一个例子，该代码只是使用同一个引擎对象，减少了部分重复操作，速度有所提高。


# # 使用Numpy 和Pandas 的简单示例

# In[60]:


from pyecharts import Bar
attr =["{}月".format(i)for i in range(1,13)]
v1 = [2.0,4.9,7.0,23.2,25.6,76.7,135.6,162.2,32.6,20.0,6.4,3.3]
v2 = [2.6,5.9,9.0,26.4,28.7,70.7,175.6,182.2,48.7,18.8,6.0,2.3]
bar=Bar("柱状图示例")
bar.add("蒸发量",attr,v1,mark_line=["average"],mark_point=["max","min"])
bar.add("降水量",attr,v2,mark_line=["average"],mark_point=["max","min"])
bar

# 图中会显示蒸发量的最大最小值，降水量的最大最小值
# mark_line=["average"] 会显示一条横线，表示该横坐标的均值，(可以设置mark_line=["max"]最大,或者最小值等)


# # 线柱图

# In[61]:


from pyecharts import Bar,Line,Overlap

attr = ['A','B','C','D']
v1 = [10,20,30,40]
v2 = [38,28,58,48]
bar = Bar("Line-Bar示例")
bar.add("barr",attr,v1)
line = Line()
line.add("line",attr,v2)

overlap = Overlap()
overlap.add(bar)
overlap.add(line)

overlap


# # 柱状图数据堆叠示例

# In[62]:


from pyecharts import Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10,25,  8,  60,20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A",attr,v1,is_stack=True)
bar.add("商家B",attr,v2,is_stack=True)
# bar.render()

# 注意： 全局配置项要在最后一个 add() 上设置，否侧设置会被冲刷掉


# # 使用标记点和标记线

# In[63]:


from pyecharts import Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10,25,  8,  60,20, 80]
bar = Bar("使用标记点和标记线")
bar.add("商家A",attr,v1,mark_point=["average"])
bar.add("商家B",attr,v2,mark_point=["min","max"])


# # 交换XY轴

# In[64]:


from pyecharts import Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10,25,  8,  60,20, 80]
bar = Bar(" 交换 XY 轴")
bar.add("商家A",attr,v1)
bar.add("商家B",attr,v2,is_convert=True)


# # X轴滚动效果

# In[65]:


import random

attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1,30) for _ in range(30)]
bar = Bar("Bar-datazoom-slider 示例")
bar.add("",attr,v1,is_label_show=True,is_datazoom_show=True)


# # 坐标轴旋转示例

# In[66]:


attr = ["{}天".format(i) for i in range(20)]
v1 = [random.randint(1, 20) for _ in range(20)]
bar = Bar("坐标轴标签旋转示例")
bar.add("", attr, v1, xaxis_interval=0, xaxis_rotate=45, yaxis_rotate=45)
# bar.render()

# 当 x 轴或者 y 轴的标签因为过于密集而导致全部显示出来会重叠的话，可采用使标签旋转的方法


# # 瀑布图示例

# In[67]:


from pyecharts import Bar

attr = ["{}月".format(i) for i in range(1, 8)]
v1 = [0, 100, 200, 300, 400, 220, 250]
v2 = [1000, 800, 600, 500, 450, 400, 300]
bar = Bar("瀑布图示例")
# 利用第一个 add() 图例的颜色为透明，即 'rgba(0,0,0,0)'，并且设置 is_stack 标志为 True
bar.add("", attr, v1, label_color=['rgba(0,0,0,0)'], is_stack=True)
bar.add("月份", attr, v2, is_label_show=True, is_stack=True, label_pos='inside')
# bar.render()


# # Bar3D（3D 柱状图）

# In[68]:


from pyecharts import Bar3D

bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
x_axis = [
    "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
    "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"
    ]
y_axis = [
    "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"
    ]
data = [
    [0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0],
    [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0], [0, 10, 0], [0, 11, 2],
    [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3], [0, 16, 4], [0, 17, 6],
    [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
    [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0],
    [1, 6, 0], [1, 7, 0], [1, 8, 0], [1, 9, 0], [1, 10, 5], [1, 11, 2],
    [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
    [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2],
    [2, 0, 1], [2, 1, 1], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0],
    [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3], [2, 11, 2],
    [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5],
    [2, 18, 5], [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4],
    [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0],
    [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4],
    [3, 12, 7], [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5],
    [3, 18, 5], [3, 19, 10], [3, 20, 6], [3, 21, 4], [3, 22, 4], [3, 23, 1],
    [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
    [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4],
    [4, 12, 2], [4, 13, 4], [4, 14, 4], [4, 15, 14], [4, 16, 12], [4, 17, 1],
    [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3], [4, 23, 0],
    [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0],
    [5, 6, 0], [5, 7, 0], [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1],
    [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11], [5, 17, 6],
    [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0],
    [6, 0, 1], [6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0],
    [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1], [6, 11, 0],
    [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0],
    [6, 18, 0], [6, 19, 0], [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]
    ]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add(
    "",
    x_axis,
    y_axis,
    [[d[1], d[0], d[2]] for d in data],
    is_visualmap=True,
    visual_range=[0, 20],
    visual_range_color=range_color,
    grid3d_width=200,
    grid3d_depth=80,
    grid3d_shading="lambert", # grid3d_shading 可以让柱状更真实
     is_grid3d_rotate=True   # 设置自动旋转
)
# bar3d.render()


# In[69]:


from pyecharts import Map

value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
attr = [
    "福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"
    ]
map = Map("Map 结合 VisualMap 示例", width=1200, height=600)
map.add(
    "",
    attr,
    value,
    maptype="china",
    is_visualmap=True,
    visual_text_color="#000",
)
# map.render()


# # 箱图

# In[70]:


from pyecharts import Boxplot

boxplot = Boxplot("箱形图")
x_axis = ['expr1', 'expr2', 'expr3', 'expr4', 'expr5']
y_axis = [
    [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880,
    1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960],
    [960, 940, 960, 940, 880, 800, 850, 880, 900, 840,
    830, 790, 810, 880, 880, 830, 800, 790, 760, 800],
    [880, 880, 880, 860, 720, 720, 620, 860, 970, 950,
    880, 910, 850, 870, 840, 840, 850, 840, 840, 840],
    [890, 810, 810, 820, 800, 770, 760, 740, 750, 760,
    910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
    [890, 840, 780, 810, 760, 810, 790, 810, 820, 850,
    870, 870, 810, 740, 810, 940, 950, 800, 810, 870]
]
_yaxis = boxplot.prepare_data(y_axis)       # 转换数据
boxplot.add("boxplot", x_axis, _yaxis)
# boxplot.render()


# In[71]:


from pyecharts import Boxplot

boxplot = Boxplot("箱形图")
x_axis = ['expr1', 'expr2']
y_axis1 = [
    [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880,
    1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960],
    [960, 940, 960, 940, 880, 800, 850, 880, 900, 840,
    830, 790, 810, 880, 880, 830, 800, 790, 760, 800],
]
y_axis2 = [
    [890, 810, 810, 820, 800, 770, 760, 740, 750, 760,
    910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
    [890, 840, 780, 810, 760, 810, 790, 810, 820, 850,
    870, 870, 810, 740, 810, 940, 950, 800, 810, 870]
]
boxplot.add("category1", x_axis, boxplot.prepare_data(y_axis1))
boxplot.add("category2", x_axis, boxplot.prepare_data(y_axis2))
# boxplot.render()


# # EffectScatter（带有涟漪特效动画的散点图）

# In[72]:


from pyecharts import EffectScatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [25, 20, 15, 10, 60, 33]
es = EffectScatter("动态散点图示例")
es.add("effectScatter", v1, v2)
# es.render()


# # 漏斗图

# In[73]:


from pyecharts import Funnel

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20, 40, 60, 80, 100, 120]
funnel = Funnel("漏斗图示例")
funnel.add(
    "商品",
    attr,
    value,
    is_label_show=True,
    label_pos="inside",
    label_text_color="#fff",
)
# funnel.render()


# In[74]:


# 漏斗图数据按升序排列
# 漏斗图数据按降序排列


from pyecharts import Funnel

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20, 40, 60, 80, 100, 120]
funnel = Funnel("漏斗图示例")
funnel.add(
    "商品",
    attr,
    value,
    is_label_show=True,
    label_pos="inside",
    label_text_color="#fff",
#     funnel_sort="ascending"  # 漏斗图数据按升序排列
    funnel_sort="descending"
)
# funnel.render()


# # 仪表盘

# In[75]:


from pyecharts import Gauge

gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 90.66)
# gauge.render("仪表盘")


# # Geo（地理坐标系）

# In[76]:


# Scatter 类型（连续型）


from pyecharts import Geo

data = [
    ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("齐齐哈尔", 14),("盐城", 15),
    ("赤峰", 16),("青岛", 18),("乳山", 18),("金昌", 19),("泉州", 21),("莱西", 21),
    ("日照", 21),("胶南", 22),("南通", 23),("拉萨", 24),("云浮", 24),("梅州", 25),
    ("文登", 25),("上海", 25),("攀枝花", 25),("威海", 25),("承德", 25),("厦门", 26),
    ("汕尾", 26),("潮州", 26),("丹东", 27),("太仓", 27),("曲靖", 27),("烟台", 28),
    ("福州", 29),("瓦房店", 30),("即墨", 30),("抚顺", 31),("玉溪", 31),("张家口", 31),
    ("阳泉", 31),("莱州", 32),("湖州", 32),("汕头", 32),("昆山", 33),("宁波", 33),
    ("湛江", 33),("揭阳", 34),("荣成", 34),("连云港", 35),("葫芦岛", 35),("常熟", 36),
    ("东莞", 36),("河源", 36),("淮安", 36),("泰州", 36),("南宁", 37),("营口", 37),
    ("惠州", 37),("江阴", 37),("蓬莱", 37),("韶关", 38),("嘉峪关", 38),("广州", 38),
    ("延安", 38),("太原", 39),("清远", 39),("中山", 39),("昆明", 39),("寿光", 40),
    ("盘锦", 40),("长治", 41),("深圳", 41),("珠海", 42),("宿迁", 43),("咸阳", 43),
    ("铜川", 44),("平度", 44),("佛山", 44),("海口", 44),("江门", 45),("章丘", 45),
    ("肇庆", 46),("大连", 47),("临汾", 47),("吴江", 47),("石嘴山", 49),("沈阳", 50),
    ("苏州", 50),("茂名", 50),("嘉兴", 51),("长春", 51),("胶州", 52),("银川", 52),
    ("张家港", 52),("三门峡", 53),("锦州", 54),("南昌", 54),("柳州", 54),("三亚", 54),
    ("自贡", 56),("吉林", 56),("阳江", 57),("泸州", 57),("西宁", 57),("宜宾", 58),
    ("呼和浩特", 58),("成都", 58),("大同", 58),("镇江", 59),("桂林", 59),("张家界", 59),
    ("宜兴", 59),("北海", 60),("西安", 61),("金坛", 62),("东营", 62),("牡丹江", 63),
    ("遵义", 63),("绍兴", 63),("扬州", 64),("常州", 64),("潍坊", 65),("重庆", 66),
    ("台州", 67),("南京", 67),("滨州", 70),("贵阳", 71),("无锡", 71),("本溪", 71),
    ("克拉玛依", 72),("渭南", 72),("马鞍山", 72),("宝鸡", 72),("焦作", 75),("句容", 75),
    ("北京", 79),("徐州", 79),("衡水", 80),("包头", 80),("绵阳", 80),("乌鲁木齐", 84),
    ("枣庄", 84),("杭州", 84),("淄博", 85),("鞍山", 86),("溧阳", 86),("库尔勒", 86),
    ("安阳", 90),("开封", 90),("济南", 92),("德阳", 93),("温州", 95),("九江", 96),
    ("邯郸", 98),("临安", 99),("兰州", 99),("沧州", 100),("临沂", 103),("南充", 104),
    ("天津", 105),("富阳", 106),("泰安", 112),("诸暨", 112),("郑州", 113),("哈尔滨", 114),
    ("聊城", 116),("芜湖", 117),("唐山", 119),("平顶山", 119),("邢台", 119),("德州", 120),
    ("济宁", 120),("荆州", 127),("宜昌", 130),("义乌", 132),("丽水", 133),("洛阳", 134),
    ("秦皇岛", 136),("株洲", 143),("石家庄", 147),("莱芜", 148),("常德", 152),("保定", 153),
    ("湘潭", 154),("金华", 157),("岳阳", 169),("长沙", 175),("衢州", 177),("廊坊", 193),
    ("菏泽", 194),("合肥", 229),("武汉", 273),("大庆", 279)]

geo = Geo(
    "全国主要城市空气质量",
    "data from pm2.5",
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color="#404a59",
)
attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    visual_range=[0, 200],
    visual_text_color="#fff",
    symbol_size=15,
    is_visualmap=True,
)
geo.render()


# In[77]:


# Scatter 类型（分段型）

geo = Geo(
    "全国主要城市空气质量",
    "data from pm2.5",
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color="#404a59",
)
attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    visual_range=[0, 200],
    visual_text_color="#fff",
    symbol_size=15,
    is_visualmap=True,
    is_piecewise=True,
    visual_split_number=6,
)
geo.render("Scatter 类型.html")


# In[78]:


# HeatMap 类型


geo = Geo(
    "全国主要城市空气质量",
    "data from pm2.5",
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color="#404a59",
)
attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    type="heatmap",
    is_visualmap=True,
    visual_range=[0, 300],
    visual_text_color="#fff",
)
geo.render("HeatMap 类型.html")


# In[79]:


# EffectScatter 类型（全国）


from pyecharts import Geo

data = [
    ("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)
]
geo = Geo(
    "全国主要城市空气质量",
    "data from pm2.5",
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color="#404a59",
)
attr, value = geo.cast(data)
geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
geo.render("EffectScatter 类型（全国）.html")


# In[80]:


# EffectScatter 类型（广东）

from pyecharts import Geo

data = [("汕头市", 50), ("汕尾市", 60), ("揭阳市", 35), ("阳江市", 44), ("肇庆市", 72)]
geo = Geo(
    "广东城市空气质量",
    "data from pm2.5",
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color="#404a59",
)
attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    maptype="广东",
    type="effectScatter",
    is_random=True,
    effect_scale=5,
    is_legend_show=False,
)
geo.render("EffectScatter 类型（广东）.html")


# # Graph（关系图）用于展现节点以及节点之间的关系数据

# In[81]:


# 关系图-力引导布局示例


from pyecharts import Graph

nodes = [{"name": "结点1", "symbolSize": 10},
         {"name": "结点2", "symbolSize": 20},
         {"name": "结点3", "symbolSize": 30},
         {"name": "结点4", "symbolSize": 40},
         {"name": "结点5", "symbolSize": 50},
         {"name": "结点6", "symbolSize": 40},
         {"name": "结点7", "symbolSize": 30},
         {"name": "结点8", "symbolSize": 20}]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get('name'), "target": j.get('name')})
graph = Graph("关系图-力引导布局示例")
graph.add("", nodes, links, repulsion=8000)
# graph.render("关系图.html")


# In[82]:


# 关系图-环形布局示例

nodes = [{"name": "结点1", "symbolSize": 10},
         {"name": "结点2", "symbolSize": 20},
         {"name": "结点3", "symbolSize": 30},
         {"name": "结点4", "symbolSize": 40},
         {"name": "结点5", "symbolSize": 50},
         {"name": "结点6", "symbolSize": 40},
         {"name": "结点7", "symbolSize": 30},
         {"name": "结点8", "symbolSize": 20}]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get('name'), "target": j.get('name')})

graph = Graph("关系图-环形布局示例")
graph.add(
    "",
    nodes,
    links,
    is_label_show=True,
    graph_repulsion=8000,
    graph_layout="circular",
    label_text_color=None,
)
# graph.render("关系图-环形布局示例.html")


# # HeatMap（热力图）热力图主要通过颜色去表现数值的大小，必须要配合 visualMap 组件使用。直角坐标系上必须要使用两个类目轴。

# In[84]:


import random
from pyecharts import HeatMap

x_axis = [
    "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
    "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
y_axis = [
    "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
heatmap = HeatMap()
heatmap.add(
    "热力图直角坐标系",
    x_axis,
    y_axis,
    data,
    is_visualmap=True,
    visual_text_color="#000",
    visual_orient="horizontal",
)
# heatmap.render("热力图.html")


# In[85]:


# 日历热力图


import datetime
import random
from pyecharts import HeatMap

begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
    for i in range((end - begin).days + 1)
]
heatmap = HeatMap("日历热力图示例", "某人 2017 年微信步数情况", width=1100)
heatmap.add(
    "",
    data,
    is_calendar_heatmap=True,
    visual_text_color="#000",
    visual_range_text=["", ""],
    visual_range=[1000, 25000],
    calendar_cell_size=["auto", 30],
    is_visualmap=True,
    calendar_date_range="2017",
    visual_orient="horizontal",
    visual_pos="center",
    visual_top="80%",
    is_piecewise=True,
)
# heatmap.render("日历热力图.html")


# # Kline/Candlestick（K线图）

# In[86]:


# 红涨蓝跌


from pyecharts import Kline

v1 = [[2320.26, 2320.26, 2287.3, 2362.94], [2300, 2291.3, 2288.26, 2308.38],
      [2295.35, 2346.5, 2295.35, 2345.92], [2347.22, 2358.98, 2337.35, 2363.8],
      [2360.75, 2382.48, 2347.89, 2383.76], [2383.43, 2385.42, 2371.23, 2391.82],
      [2377.41, 2419.02, 2369.57, 2421.15], [2425.92, 2428.15, 2417.58, 2440.38],
      [2411, 2433.13, 2403.3, 2437.42], [2432.68, 2334.48, 2427.7, 2441.73],
      [2430.69, 2418.53, 2394.22, 2433.89], [2416.62, 2432.4, 2414.4, 2443.03],
      [2441.91, 2421.56, 2418.43, 2444.8], [2420.26, 2382.91, 2373.53, 2427.07],
      [2383.49, 2397.18, 2370.61, 2397.94], [2378.82, 2325.95, 2309.17, 2378.82],
      [2322.94, 2314.16, 2308.76, 2330.88], [2320.62, 2325.82, 2315.01, 2338.78],
      [2313.74, 2293.34, 2289.89, 2340.71], [2297.77, 2313.22, 2292.03, 2324.63],
      [2322.32, 2365.59, 2308.92, 2366.16], [2364.54, 2359.51, 2330.86, 2369.65],
      [2332.08, 2273.4, 2259.25, 2333.54], [2274.81, 2326.31, 2270.1, 2328.14],
      [2333.61, 2347.18, 2321.6, 2351.44], [2340.44, 2324.29, 2304.27, 2352.02],
      [2326.42, 2318.61, 2314.59, 2333.67], [2314.68, 2310.59, 2296.58, 2320.96],
      [2309.16, 2286.6, 2264.83, 2333.29], [2282.17, 2263.97, 2253.25, 2286.33],
      [2255.77, 2270.28, 2253.31, 2276.22]]
kline = Kline("K 线图示例")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1)
# kline.render("K线图.html")


# In[87]:


# 加上水平线，dataZoom 效果

kline = Kline("K 线图示例")
kline.add(
    "日K",
    ["2017/7/{}".format(i + 1) for i in range(31)],
    v1,
    mark_point=["max"],
    is_datazoom_show=True,
)
# kline.render()


# In[88]:


# dataZoom 效果加在纵坐标轴上

kline = Kline("K 线图示例")
kline.add(
    "日K",
    ["2017/7/{}".format(i + 1) for i in range(31)],
    v1,
    mark_point=["max"],
    is_datazoom_show=True,
    datazoom_orient="vertical",
)
# kline.render()


# # Pie（饼图）饼图主要用于表现不同类目的数据在总和中的占比。每个的弧度表示数据数量的比例。

# In[89]:


from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
# pie.render()


# In[90]:


# 饼图-玫瑰图示例

from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
v2 = [19, 21, 32, 20, 20, 33]
pie = Pie("饼图-玫瑰图示例", title_pos='center', width=900)
pie.add(
    "商品A",
    attr,
    v1,
    center=[25, 50],
    is_random=True,
    radius=[30, 75],
    rosetype="radius",
)
pie.add(
    "商品B",
    attr,
    v2,
    center=[75, 50],
    is_random=True,
    radius=[30, 75],
    rosetype="area",
    is_legend_show=False,
    is_label_show=True,
)
# pie.render()


# In[91]:


# 多个饼图画在一张图内


from pyecharts import Pie,Style

pie = Pie('各类电影中"好片"所占的比例', "数据来着豆瓣", title_pos='center')
style = Style()
pie_style = style.add(
    label_pos="center",
    is_label_show=True,
    label_text_color=None
)

pie.add(
    "", ["剧情", ""], [25, 75], center=[10, 30], radius=[18, 24], **pie_style
)
pie.add(
    "", ["奇幻", ""], [24, 76], center=[30, 30], radius=[18, 24], **pie_style
)
pie.add(
    "", ["爱情", ""], [14, 86], center=[50, 30], radius=[18, 24], **pie_style
)
pie.add(
    "", ["惊悚", ""], [11, 89], center=[70, 30], radius=[18, 24], **pie_style
)
pie.add(
    "", ["冒险", ""], [27, 73], center=[90, 30], radius=[18, 24], **pie_style
)
pie.add(
    "", ["动作", ""], [15, 85], center=[10, 70], radius=[18, 24], **pie_style
)
pie.add(
    "", ["喜剧", ""], [54, 46], center=[30, 70], radius=[18, 24], **pie_style
)
pie.add(
    "", ["科幻", ""], [26, 74], center=[50, 70], radius=[18, 24], **pie_style
)
pie.add(
    "", ["悬疑", ""], [25, 75], center=[70, 70], radius=[18, 24], **pie_style
)
pie.add(
    "",
    ["犯罪", ""],
    [28, 72],
    center=[90, 70],
    radius=[18, 24],
    legend_top="center",
    **pie_style
)
# pie.render()


# # Radar（雷达图）雷达图主要用于表现多变量的数据

# In[92]:


from pyecharts import Radar

schema = [ 
    ("销售", 6500), ("管理", 16000), ("信息技术", 30000),
    ("客服", 38000), ("研发", 52000), ("市场", 25000)
]
v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
radar = Radar()
radar.config(schema)
radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False,
          legend_selectedmode='single')
# radar.render()


# # Scatter（散点图）直角坐标系上的散点图可以用来展现数据的 x，y 之间的关系，如果数据项有多个维度，可以用颜色来表现，利用 geo 组件。

# In[93]:


from pyecharts import Scatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [10, 20, 30, 40, 50, 60]
scatter = Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add("B", v1[::-1], v2)
# scatter.render()


# In[94]:


# 利用 Visualmap 组件，通过颜色映射数值
scatter = Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add("B", v1[::-1], v2, is_visualmap=True)
# scatter.render()


# In[95]:


# 利用 Visualmap 组件，通过图形点大小映射数值

scatter = Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add(
    "B",
    v1[::-1],
    v2,
    is_visualmap=True,
    visual_type="size",
    visual_range_size=[20, 80],
)


# # Scatter3D（3D 散点图）

# In[96]:


from pyecharts import Scatter3D

import random
data = [
    [random.randint(0, 100),
    random.randint(0, 100),
    random.randint(0, 100)] for _ in range(80)
]
range_color = [
    '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
    '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
scatter3D = Scatter3D("3D 散点图示例", width=1200, height=600)
scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
# scatter3D.render()


# # Surface3D（3D 曲面图）

# In[97]:


import math

from pyecharts import Surface3D


def create_surface3d_data():
    for t0 in range(-60, 60, 1):
        y = t0 / 60
        for t1 in range(-60, 60, 1):
            x = t1 / 60
            if math.fabs(x) < 0.1 and math.fabs(y) < 0.1:
                z = '-'
            else:
                z = math.sin(x * math.pi) * math.sin(y * math.pi)
            yield [x, y, z]

range_color = [
    "#313695",
    "#4575b4",
    "#74add1",
    "#abd9e9",
    "#e0f3f8",
    "#ffffbf",
    "#fee090",
    "#fdae61",
    "#f46d43",
    "#d73027",
    "#a50026",
]

_data = list(create_surface3d_data())
surface3d = Surface3D("3D 曲面图示例", width=1200, height=600)
surface3d.add(
    "",
    _data,
    is_visualmap=True,
    visual_range_color=range_color,
    visual_range=[-3, 3],
    grid3d_rotate_sensitivity=5,
)
# surface3d.render()


# # WordCloud（词云图）

# In[98]:


from pyecharts import WordCloud

name = [
    'Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
    'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
    'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
    'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value = [
    10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
    965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])
# wordcloud.render()

