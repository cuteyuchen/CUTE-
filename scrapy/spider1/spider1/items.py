# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Movies(scrapy.Item):
    id=scrapy.Field()#id字段
    kind=scrapy.Field()# 类别（电影，欧美电影.....）
    img_url=scrapy.Field()# 电影图片链接
    name=scrapy.Field()# 电影名字
    actors=scrapy.Field()# 演员
    definition=scrapy.Field()# 清晰度
    area=scrapy.Field()# 地区
    language=scrapy.Field()# 语言
    director=scrapy.Field()#导演
    years = scrapy.Field()  # 更新日期
    show_date=scrapy.Field()#上映日期
    movie_time=scrapy.Field()#片长
    douban_score=scrapy.Field()#豆瓣评分
    des=scrapy.Field()#影片描述
    download_urls=scrapy.Field()#下载前面的描述和下载链接字典
    m3u8_online=scrapy.Field()#m3u8在线播放链接
    yunbo_online=scrapy.Field()#yunbo在线播放链接
