from django.shortcuts import render,HttpResponse
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
import json
import random


# Create your views here.
def render_page(request,page_name):
    return render(request,page_name)


# 获取所有电影
class Movies(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


#电影搜索 按照电影名字模糊匹配
class search(generics.ListAPIView):
    queryset = {}
    serializer_class = MovieSerializer
    def get(self, request, *args, **kwargs):
        movie_data = []
        name = request.GET.get('kw')
        page = request.GET
        queryset1 = Movie.objects.filter(m3u8_online__ne={},name__contains=name)
        queryset2 = Movie.objects.filter(m3u8_online__ne={},actors__contains=name)
        queryset3 = Movie.objects.filter(m3u8_online__ne={},director__contains=name)
        movie1 = MovieSerializer(queryset1,many=True)
        movie2 = MovieSerializer(queryset2,many=True)
        movie3 = MovieSerializer(queryset3,many=True)
        movie_data.extend(movie1.data)
        movie_data.extend(movie2.data)
        movie_data.extend(movie3.data)
        if len(movie_data)!=0:
            news_li = []
            for i in movie_data:
                if i not in news_li:
                    news_li.append(i)
            return Response(news_li)
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class Area(generics.ListAPIView):
    queryset = {}
    serializer_class = MovieSerializer
    def get(self, request, *args, **kwargs):
        kw=request.GET.get('kw')
        queryset=Movie.objects.filter(m3u8_online__ne={},area=kw)
        movie=MovieSerializer(queryset,many=True)
        return Response(movie.data)

class language(generics.ListAPIView):
    queryset = {}
    serializer_class = MovieSerializer
    def get(self, request, *args, **kwargs):
        kw=request.GET.get('kw')
        print(kw)
        queryset=Movie.objects.filter(m3u8_online__ne={},language=kw)
        movie=MovieSerializer(queryset,many=True)
        return Response(movie.data[0:500])

class IndexRecommend_img(generics.ListAPIView):
    queryset = {}
    serializer_class = MovieSerializer
    def get(self, request, *args, **kwargs):
        kw = request.GET.get('kw','')
        num = int(request.GET.get('num',8))
        if kw=='电影':
            data_num=500
        else:
            data_num=100
        queryset = Movie.objects.filter(m3u8_online__ne={},kind__contains=kw, years__in=('2019',)).order_by('-douban_score')
        movie = MovieSerializer(queryset, many=True)
        list1 = movie.data[0:data_num]
        random.shuffle(list1)
        return Response(list1[0:num])


class IndexRecommend_text(generics.ListAPIView):
    queryset = {}
    serializer_class = MovieSerializer
    def get(self, request, *args, **kwargs):
        kind=request.GET.get('kind','电影')
        num=request.GET.get('num',10)
        print(kind)
        if '首页' in kind:
            kind=kind.replace('首页','')
            queryset = Movie.objects.filter(m3u8_online__ne={},kind__contains=kind, years__in=('2019',))
        else:
            queryset = Movie.objects.filter(m3u8_online__ne={},kind=kind)
        movie = MovieSerializer(queryset,many=True)
        print(kind)
        print(len(movie.data))
        if len(movie.data)>0:
            if kind == '电影':
                data_num = 500
            else:
                data_num = 100
            movie_datas = movie.data[0:data_num]
            random.shuffle(movie_datas)
            return Response(movie_datas[0:num])
        else:
            return Response({'code':status.HTTP_404_NOT_FOUND})


class QueryMovie(generics.ListAPIView):
    queryset = {}
    serializer_class = MovieSerializer
    def get(self, request, *args, **kwargs):
        sort = request.GET.get('sort','')
        year = request.GET.get('year','')
        kind = request.GET.get('kind','电影')
        page = int(request.GET.get('page','1'))
        if sort=='' and year=='':
            queryset = Movie.objects.filter(m3u8_online__ne={},kind=kind)
            movie = MovieSerializer(queryset, many=True)
            return Response(movie.data[(page - 1) * 24:page * 24])
        elif sort==''and year!='':
            print(kind,year)
            queryset = Movie.objects.filter(m3u8_online__ne={},kind=kind,years=year)
            movie = MovieSerializer(queryset, many=True)
            return Response(movie.data[(page-1)*24:page*24])
        elif sort!=''and year=='':
            queryset = Movie.objects.filter(m3u8_online__ne={},kind=kind).order_by(sort)
            movie = MovieSerializer(queryset, many=True)
            return Response(movie.data[(page - 1) * 24:page * 24])
        else:
            queryset = Movie.objects.filter(m3u8_online__ne={},kind=kind, years=year).order_by(sort)
            movie = MovieSerializer(queryset, many=True)
            return Response(movie.data[(page - 1) * 24:page * 24])


# 获取指定演员的电影
class actorMovie(generics.ListAPIView):
    queryset = {}
    serializer_class = MovieSerializer
    def get(self, request, *args, **kwargs):
        actor = request.GET.get('actor','')
        if actor!='':
            queryset = Movie.objects.filter(m3u8_online__ne={},actors__contains=actor)
            movie = OneMovieSerializer(queryset,many=True)
            return Response(movie.data)


class get_pages(generics.ListAPIView):
    queryset = {}
    serializer_class = MovieSerializer
    def get(self, request, *args, **kwargs):
        kind = request.GET.get('kind','')
        year = request.GET.get('year','')
        if kind!='' and year=='':
            queryset = Movie.objects.filter(m3u8_online__ne={},kind=kind)
            movie = MovieSerializer(queryset, many=True)
            pages = len(movie.data)
            return Response(pages)
        elif kind!='' and year!='':
            queryset = Movie.objects.filter(m3u8_online__ne={},kind=kind,years=year)
            movie = MovieSerializer(queryset, many=True)
            pages = len(movie.data)
            return Response(pages)
        else:
            return Response({'code':status.HTTP_404_NOT_FOUND})


class one_movie(generics.ListAPIView):
    queryset = {}
    serializer_class = MovieSerializer
    def get(self, request, *args, **kwargs):
        name = request.GET.get('name')
        print(name)
        if name:
            queryset = Movie.objects.get(_id=name)
            movie = OneMovieSerializer(queryset)
            return Response(movie.data)






