import urllib.request    # 需要安装 urllib 库
from bs4 import BeautifulSoup    #需要安装 bs4 库


def get_weather(city_pinyin):
    # 声明头，模拟真人操作，防止被反爬虫发现
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64;\
    rv:23.0) Gecko/20100101 Firefox/23.0'}
    # 通过传入的城市名拼音参数来拼接出该城市的天气预报的网页地址
    website = "http://www.tianqi.com/" + city_pinyin + ".html"
    req = urllib.request.Request(url=website, headers=header)
    page = urllib.request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html.decode("utf-8"), "html.parser")
    # html.parser表示解析使用的解析器
    nodes = soup.find_all('dd')
    tody_weather = ""
    for node in nodes:  # 遍历获取各项数据
        temp = node.get_text()
        if (temp.find('[切换城市]')):
            temp = temp[:temp.find('[切换城市]')]
        tody_weather += temp
    # 去除字符串中的空行:
    tianqi = "".join([s for s in tody_weather.splitlines(True)
                      if s.strip()])

    return tianqi  # 返回结果

# 调用封装号好的函数获取天气预报，参数‘京山’是拼音：
print(get_weather('jingshan')) 
# 想查询哪个城市的天气情况，直接将参数替换为它的拼音即可
