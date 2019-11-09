#rest_framework_mongoengine是专门针对MongoDB数据库构建的rest_framework框架，该框架内部完成对MongoDB数据的序列化操作
from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import *
# 每个电影的序列化器
class MovieSerializer(DocumentSerializer):
    class Meta:
        model = Movie
        fields = ('_id','name','kind','img_url','douban_score','des','definition','show_date','years')

class OneMovieSerializer(DocumentSerializer):
    class Meta:
        model = Movie
        fields = ('_id','name','kind','img_url','area','director','actors','douban_score','des','definition','show_date','download_urls','m3u8_online','yunbo_online','years','language')