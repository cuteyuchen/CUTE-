# -*- coding: utf-8 -*-
import scrapy,re,urllib.parse
from scrapy import Request
from ..items import Movies


class SpidermoviesSpider(scrapy.Spider):
    name = 'spidermovies'
    allowed_domains = ['www.27k.cc']
    start_urls = ['http://www.27k.cc']
    online_url='https://zuidajiexi.net/m3u8.html?url='

    def parse(self, response):
        sort_urls = response.xpath('//*[@id="responsive-navbar"]/ul/li/a/@href').extract()
        sort_titles = response.xpath('//*[@id="responsive-navbar"]/ul/li/a/text()').extract()
        for i in range(len(sort_urls)):
            yield Request(url=self.start_urls[0]+sort_urls[i], callback=self.parse_page_datas,
                          meta={'url': self.start_urls[0]+sort_urls[i], 'kind': sort_titles[i]})

    def parse_page_datas(self, response):
        # 获取当前分类的总页数
        totle_pages = response.xpath('//*[@id="pager"]/nav/ul/text()[1]').extract()[0]
        totle_pages_num=int(''.join(re.findall('\d',(re.split('/',totle_pages))[-1])))
        # 获取当前分类页面的url
        commom_path = response.meta.get('url')
        # 循环遍历总页数，发起二级页面请求
        for i in range(1, totle_pages_num + 1):
            next_url = commom_path[:-5] +'-pg-{0}.html'.format(i)
            # print(next_url)
            yield Request(url=next_url, callback=self.next_pages, meta={'url': commom_path,'kind': response.meta.get('kind')})

    def next_pages(self, response):
        # 获取当前页面所有的视频的链接
        items = response.xpath('//*[@id="mainbody"]/div/div[1]/a/@href').extract()
        img_urls=response.xpath('//*[@id="mainbody"]/div/div[1]/a/img/@src').extract()
        for i in range(len(items)):
            movie = Movies()
            current_url = self.start_urls[0]+items[i]
            if 'http' not in img_urls[i]:
                movie['img_url'] =self.start_urls[0]+ img_urls[i]
            else:
                movie['img_url'] = img_urls[i]
            yield Request(url=current_url, callback=self.parse2,meta={'movie':movie,'url':current_url,'kind': response.meta.get('kind')})

    def parse2(self, response):
        try:
            current_url=response.meta.get('url')
            current_url='/'.join((current_url.split('/'))[:-1])
            movie=response.meta.get('movie')
            try:
                movie['id']=int((((re.split('/',response.meta.get('url')))[-1]).split('.'))[0])
            except:
                movie['id']='未知'
            try:
                movie['kind']=response.meta.get('kind')
            except:
                movie['kind']='未知'
            # try:
            #     movie['img_url'] = response.xpath('//*[@id="poster"]/a/img/@src').extract()[0]
            # except:
            #     movie['img_url']='未知'
            try:
                movie['name']=((response.xpath('//*[@id="movie_name"]/text()').extract()[0]).replace('\n ','')).replace(' ','')
            except:
                movie['name'] ='未知'
            try:
                movie['actors']=response.xpath('//*[@id="movie_aka"]/text()').extract()[0]
            except:
                movie['actors'] ='未知'
            try:
                movie['definition']=((response.xpath('//*[@id="movie_name"]/small/span[1]/text()').extract()[0]).replace('\n ','')).replace(' ','')
            except:
                movie['definition'] ='未知'
            try:
                movie['area'] = response.xpath('//*[@id="mainbody"]/p[3]/a[2]/text()').extract()[0]
            except:
                movie['area'] ='未知'
            try:
                movie['language'] =response.xpath('//*[@id="mainbody"]/p[3]/a[3]/text()').extract()[0]
            except:
                movie['language'] ='未知'
            try:
                movie['director'] = response.xpath('//*[@id="mainbody"]/p[4]/a[7]/text()').extract()[0]
            except:
                movie['director'] ='未知'
            try:
                years=((response.xpath('//*[@id="movie_name"]/small/text()').extract()[0]).replace('\n ','')).replace(' ','')
                years=''.join(re.findall('\d',years))
                movie['years'] = years
            except:
                movie['years'] ='未知'
            try:
                movie['show_date']=((response.xpath('//*[@id="mainbody"]/p[3]/text()[13]').extract()[0]).replace('\n ','')).replace(' ','')
            except:
                movie['show_date']='未知'
            try:
                movie['movie_time'] = ((response.xpath('//*[@id="mainbody"]/p[3]/text()[11]').extract()[0]).replace('\n ','')).replace(' ','')
            except:
                movie['movie_time'] ='未知'
            try:
                douban_score=response.xpath('//*[@id="mainbody"]/p[3]/span[8]/text()').extract()[0]
                douban_score = re.findall('\d', douban_score)
                if len(douban_score) == 1:
                    douban_score = douban_score[0]
                elif len(douban_score) == 2:
                    douban_score = '.'.join(douban_score)
                else:
                    douban_score = ''.join(douban_score[0:-1]) + '.' + douban_score[-1]
                movie['douban_score'] = douban_score
            except:
                movie['douban_score'] ='未知'
            try:
                movie['des'] = (response.xpath('//*[@id="files"]/p[2]/text()').extract()[0]).strip()
            except:
                movie['des'] ='未知'
            try:
                urls_dic={}
                url_names= response.xpath('//*[@id="files"]/div[2]/table//tr/td/div/div[1]/a/text()').extract()
                download_urls = response.xpath('//*[@id="files"]/div[2]/table//tr/td/div/div[1]/a/@href').extract()
                for i in range(len(url_names)):
                    # if '//' not in download_urls[i]:
                    #     download_url=current_url+'/'+download_urls[i]
                    # else:
                    download_url=(download_urls[i]).replace('\n','')
                    urls_dic[url_names[i].replace('.','点')]=download_url
                movie['download_urls']=urls_dic
            except:
                movie['download_urls'] ='未知'
            movie['m3u8_online'] = {}
            movie['yunbo_online'] = {}
            online_url=response.xpath('//*[@id="mainbody"]/div[2]/a/@href').extract()
            if len(online_url)==0:
                yield movie
            else:
                yield Request(url=self.start_urls[0]+online_url[0],callback=self.parse3,meta={'movie':movie})
        except Exception as e:
            print(e)

    def parse3(self,response):
        # m3u8链接字典
        m3u8_dic={}
        # yunbo链接字典
        yunbo_dic={}
        # 获取链接所在的script文本
        script=response.xpath('//p/script/text()').extract()[0]
        print('================================================')
        print(script)
        st = script.replace('%u', '\\u')
        k = urllib.parse.unquote(st.encode().decode('unicode-escape'))
        k = k.split('\'')
        m = (k[-2]).split('$$$')
        if len(m)==2:
            m3u8 = m[0]
            yunbo = m[1]
            m3u8 = re.split('[$#]', m3u8)
            print(m3u8)
            yunbo = re.split('[$#]', yunbo)
            print(yunbo)
            new_m3u8 = m3u8
            new_yunbo = yunbo
            for i in range(0, len(m3u8), 2):
                if 'http' in m3u8[i]:
                    new_m3u8.insert(i, '第{0}集'.format(int(i / 2) + 1))
            print(new_m3u8)
            for i in range(0, len(yunbo), 2):
                if 'http' in yunbo[i]:
                    new_yunbo.insert(i, '第{0}集'.format(int(i / 2) + 1))
            print(new_yunbo)
            for i in range(0, len(new_m3u8), 2):
                m3u8_dic[new_m3u8[i]] = self.online_url+new_m3u8[i + 1]
            for i in range(0, len(new_yunbo), 2):
                yunbo_dic[new_yunbo[i]] = new_yunbo[i + 1]
        else:
            m3u8 = m[0]
            m3u8 = re.split('[$#]', m3u8)
            new_m3u8 = m3u8
            for i in range(0, len(m3u8), 2):
                if 'http' in m3u8[i]:
                    new_m3u8.insert(i, '第{0}集'.format(int(i / 2) + 1))
            print(new_m3u8)
            for i in range(0, len(new_m3u8), 2):
                m3u8_dic[new_m3u8[i]] =self.online_url+ new_m3u8[i + 1]


        # m = re.sub('\$+', '!', m)
        # # m3u8和yunbo链接列表
        # online_urls_list = re.split('[!#]', m)
        # print(online_urls_list,len(online_urls_list))
        # list_num=int(len(online_urls_list)/2)
        # print(list_num)
        # m3u8_list=online_urls_list[0:list_num]
        # print(m3u8_list)
        # yunbo_list=online_urls_list[list_num:]
        # for i in range(0,list_num,2):
        #     m3u8_dic[m3u8_list[i].replace('.','点')] = self.online_url+m3u8_list[i + 1]
        #     yunbo_dic[yunbo_list[i].replace('.','点')]=self.online_url+yunbo_list[i+1]

        movie=response.meta.get('movie')
        movie['m3u8_online']=m3u8_dic
        movie['yunbo_online']=yunbo_dic
        yield movie

