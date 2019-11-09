<template>
    <div class='detail'>
       <div class='head1'>
           <div class="head_sort">
               <div class="contain">
                <ul>
                    <li class="logo_img">
                        <router-link to="/head1">
                            <img src="../assets/img/logo.png" alt="" height="45px">
                            <img src="../assets/img/logo1.png" alt="" height="45px">
                        </router-link>
                    </li>
                    <li v-for="(item, index) in sort" :key="index" class="sort_rou">
                        <router-link :to="{path:'/movie',query:{kind:item}}" class="rou">
                             {{item}} 
                        </router-link>
                    </li>
                </ul> 
                <!-- input输入框 -->
                <div class="enter">
                    <input type="text" placeholder="请输入电影名……" class="type" v-model="input_text" @input="change()">
                    <el-button slot="append" icon="el-icon-search" size="small" @click="input" class="pos"></el-button>
                    <!-- <button class="iconfont pos" >&#xe606;</button> -->
                </div>   
            </div>
           </div>
        </div> 
        <div class="totals">
            <div class="img_info">
                <div class="detailed_img">
                    <img v-lazy=movie_detail.img_url :src=movie_detail.img_url :onerror="default_img_url" alt="">
                </div>
                <div class="detailed_info">
                    <div class="detailed_info_name">{{movie_detail.name}}</div>
                    <div class="detailed_info_2">类型：<router-link :to="{path:'/movie',query:{kind:movie_detail.kind}}" class="detailed_info_p">{{movie_detail.kind}}</router-link></div>
                    <div class="detailed_info_2">地区：<span class="detailed_info_p">{{movie_detail.area}}</span></div>
                    <div class="detailed_info_2">语言：<span class="detailed_info_p">{{movie_detail.language}}</span></div>
                    <br>
                    <div class="detailed_info_2">片长：<span class="detailed_info_p">{{movie_detail.movie_time}}</span></div>
                    <div class="detailed_info_2">上映日期：<span class="detailed_info_p">{{movie_detail.show_date}}</span></div>
                    <div class="detailed_info_2">资源更新：<span class="detailed_info_p">{{movie_detail.years}}</span></div> <br>
                    <div class="detailed_info_2">豆瓣评分：<span class="gold1">{{movie_detail.douban_score}}</span></div> <br>
                    <div class="detailed_info_2">演员：
                        <router-link 
                            class="detailed_info_p" v-for="(item,index4) in res_actor" :key="index4" 
                            :to="{path:'/search',
                            query:{
                                search_text:item
                            }}">
                            {{item}}
                        </router-link>
                    </div>
                    <br>
                    <template v-if="res_director!='未知'">
                        <div class="detailed_info_2">导演：
                            <router-link class="detailed_info_p" v-for="(item,index5) in res_director" :key="index5" 
                            :to="{path:'/search',
                                query:{
                                    search_text:item
                                }}">
                                {{item}}
                            </router-link>
                        </div>
                        <br>
                        <div class="detailed_info_2">介绍：<span class="detailed_info_p">{{movie_detail.des | ellipsis}}</span></div>
                    </template>
                    
                </div>
            </div>
            <div class="z_play_online">
                <div class="online" @click="both(0)" :class="{online_select:online_index==0}">在线播放</div>
                <div class="online" @click="both(1)" :class="{online_select:online_index==1}">迅雷下载</div>
                <hr style="width:100%;margin-bottom:10px">
                <div class="first_2" v-for="(value,key, index1) in movie_detail.m3u8_online" :key="index1" :class="{first_2_show:online_index==0}">
                    <router-link :to="{path:'/mp4',query:{name:movie_detail._id,iframe_url:value}}">{{key}}
                    </router-link>
                </div>                    
                <div class="first_2" v-for="(value1,key1, index2) in movie_detail.download_urls" :key="index2" :class="{first_2_show:online_index==1}">
                    <a :href=value1>{{key1}}</a>
                </div>   
            </div>                    
            <div class="movie2">
                <div class="re_bo">相关热播</div>
                <div class="mark" v-for="(item,index) in canshu_1" :key="index">
                    <div class="like">
                        <a @click.prevent="fngoTo(item._id)" href="">
                            <img v-lazy=item.img_url :src=item.img_url :onerror="default_img_url" alt="" v-bind:style='{width:"100%",height:"100%"}'>
                        </a>
                        <span class="gold">{{item.douban_score}}</span>
                        <span class="episode">{{item.definition}}</span>
                    </div>
                    <div class="mov_title">
                        <a @click.prevent="fngoTo(item._id)" href="">{{item.name}}</a>
                    </div>
                </div>
            </div>
        </div>
        <div style="background:rgb(51,51,51);padding-top:30px;height:100px;text-align:center;color:#999999;margin-top:30px">本网站内容收集于互联网，刘震.PY不承担任何由于内容的合法性及健康性所引起的争议和法律责任。<br>
本站永久免费更新最新电影与剧集，欢迎大家使用并推荐朋友。</div>
    </div>
</template>

<script>
export default {
    name:'mp4',
    filters: {
        ellipsis (value) {
        if (!value) return ''
        if (value.length > 55) {
            return value.slice(0,55) + '...'
        }
        return value
        }
    },
    data() {
        return {
            sort:["电影","欧美电影","日韩电影","港台电影","大陆电影","动漫","日韩剧","港台剧","大陆剧","欧美剧","综艺"],
            sort1:[],
            movie_detail:'',
            res_actor:'',
            res_director:'',
            canshu_1:'',
            online_index:0,
            default_img_url:'this.src="'+require('../assets/img/default.jpg')+'"',
            input_text:''
        }
    },
    methods: {
        toTop() {
            let top = document.documentElement.scrollTop || document.body.scrollTop;
                // 实现滚动效果 
                const timeTop = setInterval(() => {
                    document.body.scrollTop = document.documentElement.scrollTop = top -= 50;
                    if (top <= 0) {
                    clearInterval(timeTop);
                    }
            }, 10);
        },
        both(index){
            this.online_index=index
        },
        input(){
            console.log(this.input_text)
            if (this.input_text != ''){
                this.$router.push({
                    path:'/search',
                    query:{
                        search_text:this.input_text
                    }
                })
            }
        },
        fngoTo(name){
            this.online_index=0
            console.log(name)
            this.$http.get(this.$store.state.baseUrl+'/app01/one_movie/?name='+name)
            .then((res2)=>{
                this.movie_detail=res2.data
                this.res_actor = res2.data.actors.split(',')
                this.res_director = res2.data.director.split(',')
                this.toTop()
            })
            .catch((res2)=>{
                console.log("失败的回调111",res2)
            })
        },
        get_movie_detail(name){
            document.body.scrollTop = document.documentElement.scrollTop = 0;
            this.$http.get(this.$store.state.baseUrl+'/app01/one_movie/?name='+this.$route.query.name)
            .then((res)=>{
                this.movie_detail=res.data,
                this.res_actor = res.data.actors.split(',')
                this.res_director = res.data.director.split(',')
                this.$http.get(this.$store.state.baseUrl+"/app01/indexrecommend_text/?kind="+res.data.kind)
                .then((res1)=>{
                    this.canshu_1=res1.data.slice(0,6);
                    console.log(this.canshu_1)
                })
                .catch((res1)=>{
                    console.log("失败的回调111",res1)
                })
            })
            .catch((res)=>{
                console.log('失败的回调222',res)
            })
        },
        change(){
            let _this = this;
            document.onkeydown = function(e){
                let _key = window.event.keyCode;
                if(_key === 13){
                    _this.input()
                }
            }
        }
    },
    mounted(){
        this.get_movie_detail(this.$route.query.name)
    }
}
</script>

<style scoped>
@import url("../assets/css/detail.css");
@import url("../assets/css/font.css");
@import url("../assets/css/logo.css");
</style>
