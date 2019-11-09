from django.db import models
import mongoengine
# Create your models here.
class Movie(mongoengine.Document):
    _id = mongoengine.ObjectIdField()
    id = mongoengine.IntField(max_length=100)#id字段
    kind = mongoengine.StringField(max_length=250)# 类别
    name = mongoengine.StringField(max_length=250)# 电影名字
    img_url = mongoengine.StringField(max_length=250)# 电影图片链接
    actors = mongoengine.StringField(max_length=250)# 演员
    definition = mongoengine.StringField(max_length=250)# 清晰度
    language = mongoengine.StringField(max_length=250)# 语言
    area = mongoengine.StringField(max_length=250)# 地区
    director = mongoengine.StringField(max_length=250)# 导演
    show_date = mongoengine.StringField(max_length=250)#上映日期
    years = mongoengine.StringField(max_length=250)#更新日期
    movie_time = mongoengine.StringField(max_length=250)#片长
    douban_score = mongoengine.StringField(max_length=250)#豆瓣评分
    des = mongoengine.StringField(max_length=250)#影片描述
    download_urls = mongoengine.DictField(max_length=250)#下载链接
    m3u8_online = mongoengine.DictField(max_length=250)#m3u8在线播放链接
    yunbo_online = mongoengine.DictField(max_length=250)# 在线播放链接

    meta = {'collection':'movies_data'}
