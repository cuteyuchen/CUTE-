"""M_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('movie/',Movies.as_view(),name='movie'),
    path('search/',search.as_view(),name='search'),
    path('index_recommend_img/',IndexRecommend_img.as_view(),name='recommend'),
    path('querymovie/',QueryMovie.as_view(),name='querymovie'),
    path('get_pages/',get_pages.as_view(),name='get_pages'),
    path('render/<str:page_name>/', render_page),
    path('indexrecommend_text/', IndexRecommend_text.as_view(),name='indexrecommend_text'),
    path('one_movie/', one_movie.as_view(),name='one_movie'),
    path('area/', Area.as_view(),name='area'),
    path('language/', language.as_view(),name='language'),
]
