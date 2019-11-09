<template>
    <div class="heads">
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
        <div class="movie1">
            <!-- 轮播图设计 -->
            <swiper class="swiper" :options="swiperOption"  ref="mySwiper">
                <!-- slides -->
                <swiper-slide>
                     <!--第一块轮播图  -->
                    <div class="mov_1" v-bind:style='{display:"block"}'>
                        <!-- 上边的图片以及标题 -->
                        <div class="mov_1_son" v-for="(item,index) in dt" :key="index">
                            <!-- 图片 -->
                            <div class="like">
                                <router-link :to="{path:'./detail',query:{name:item._id}}">
                                    <img v-lazy=item.img_url :src=item.img_url :onerror="default_img_url" alt="" v-bind:style='{width:"100%",height:"100%"}'>  
                                </router-link>    
                                <span class="gold">{{item.douban_score}}</span>
                                <span class="episode">{{item.definition | ellipsis}}</span>
                            </div>
                            <!-- 标题 -->
                            <div class="mov_title">
                                <h4>
                                    <span>
                                        <router-link :to="{path:'./detail',query:{name:item._id}}">
                                            {{item.name}}
                                        </router-link>
                                    </span>
                                </h4>
                            </div>
                        </div>
                    </div>
                </swiper-slide>
                <swiper-slide> 
                    <!--第二块轮播图  -->
                    <div class="mov_1 map1" v-bind:style='{display:"block"}'>
                        <!-- 上边的图片以及标题 -->
                        <div class="mov_1_son" v-for="(item,index) in dt1" :key="index">
                            <!-- 图片 -->
                            <div class="like">
                                <router-link :to="{path:'./detail',query:{name:item._id}}">
                                    <img v-lazy=item.img_url :src=item.img_url :onerror="default_img_url" alt="" v-bind:style='{width:"100%",height:"100%"}'>
                                </router-link>    
                                <span class="gold">{{item.douban_score}}</span>
                                <span class="episode">{{item.definition | ellipsis}}</span>
                            </div>
                            <!-- 标题 -->    
                            <div class="mov_title">
                                <h4>
                                    <span>
                                        <router-link :to="{path:'./detail',query:{name:item._id}}">
                                            {{item.name}}
                                        </router-link>
                                    </span>
                                </h4>
                            </div>
                        </div>
                    </div>
                </swiper-slide>
                <!-- 第三块轮播图 -->
                <swiper-slide> 
                    <div class="mov_1 map1" style='{display:"block"}'>
                        <div class="mov_1_son" v-for="(item,index) in dt2" :key="index">
                            <div class="like">
                                <router-link :to="{path:'./detail',query:{name:item._id}}">
                                    <img v-lazy=item.img_url :src=item.img_url :onerror="default_img_url" alt="" v-bind:style='{width:"100%",height:"100%"}'>
                                </router-link>
                                <span class="gold">{{item.douban_score}}</span>
                                <span class="episode">{{item.definition | ellipsis}}</span>
                            </div>
                            <div class="mov_title">
                                <h4>
                                    <span>
                                        <router-link :to="{path:'./detail',query:{name:item._id}}">
                                            {{item.name}}
                                        </router-link>
                                    </span>
                                </h4>
                            </div>
                        </div>
                    </div>
                </swiper-slide>
                <!-- Optional controls -->
                <div class="swiper-pagination" slot="pagination"></div>
            </swiper>


        </div>
        <div class="title">
            <div class="new_m">
                <h3 class="h3">
                    <span>最新电影</span>
                </h3>
            </div>
            <div class="more">
                <router-link :to="{
                            path:'/movie',
                            query:{kind:'电影'}
                        }">
                                    更多>>
                </router-link>    
            </div>
        </div>
        <div class="con">
            <div class="movie2">
                <div class="mark" v-for="(item,index) in dt3" :key="index">
                    <div class="like">
                        <router-link :to="{path:'/detail',query:{name:item._id}}">
                            <img v-lazy=item.img_url :src=item.img_url :onerror="default_img_url" alt="" v-bind:style='{width:"100%",height:"100%"}'>
                        </router-link>
                        <span class="gold">{{item.douban_score}}</span>
                        <span class="episode">{{item.definition | ellipsis}}</span>
                    </div>
                    <div class="mov_title">
                        <h4 v-bind:style='{margin:"0"}'><router-link :to="{path:'./detail',query:{name:item._id}}">{{item.name}}</router-link></h4>
                    </div>
                </div>
            </div>
            <div class="rank">
                <ul class="ul_rank">
                    <li v-for="(item,index) in dt4" :key="index">
                        <span class="m1">{{item.kind}}</span>
                        <router-link :to="{path:'/detail',query:{name:item._id}}" class="m2">{{item.name}}</router-link>
                        <span class="m3">{{item.definition}}</span>
                    </li>
                </ul>
            </div>
        </div>
        <hr v-bind:style='{width:"1137px",margin:"0 auto"}'>
        <div class="title">
            <div class="new_m">
                <h3 class="h3">
                    <span style="width:120px">
                        最新电视剧
                    </span>
                </h3>
            </div>
            <div class="more">
                <router-link :to="{
                            path:'/movie',
                            query:{kind:'大陆剧'}
                        }">
                更多>>
                </router-link>    
            </div>
        </div>
        <div class="con">
            <div class="movie2">
                <div class="mark" v-for="(item,index) in dt5" :key="index">
                    <div class="like">
                        <router-link :to="{path:'/detail',query:{name:item._id}}">
                            <img v-lazy=item.img_url :src=item.img_url :onerror="default_img_url" alt="" v-bind:style='{width:"100%",height:"100%"}'>
                        </router-link>
                        <span class="gold">{{item.douban_score}}</span>
                        <span class="episode">{{item.definition | ellipsis}}</span>
                    </div>
                    <div class="mov_title">
                        <h4 v-bind:style='{margin:"0"}'><router-link :to="{path:'./detail',query:{name:item._id}}">{{item.name}}</router-link></h4>
                    </div>
                </div>
            </div>
            <div class="rank">
                <ul class="ul_rank">
                    <li v-for="(item,index) in dt8" :key="index">
                        <span class="m1">{{item.kind}}</span>
                        <router-link :to="{path:'/detail',query:{name:item._id}}" class="m2">{{item.name}}</router-link>
                        <span class="m3">{{item.definition}}</span>
                    </li>
                </ul>
            </div>
        </div>
        <hr v-bind:style='{width:"1137px",margin:"0 auto"}'>
        <div class="title">
            <div class="new_m">
                <h3 class="h3">
                    <span>最新动漫</span>
                </h3>
            </div>
            <div class="more">
                <router-link :to="{
                            path:'/movie',
                            query:{kind:'动漫'}
                        }">更多>></router-link>   
            </div>
        </div>
        <div class="con">
            <div class="movie2">
                <div class="mark" v-for="(item,index) in dt6" :key="index">
                    <div class="like">
                        <router-link :to="{path:'./detail',query:{name:item._id}}">
                            <img v-lazy=item.img_url :src=item.img_url :onerror="default_img_url" alt="" v-bind:style='{width:"100%",height:"100%"}'>
                        </router-link>
                        <span class="gold">{{item.douban_score}}</span>
                        <span class="episode">{{item.definition | ellipsis}}</span>
                    </div>
                    <div class="mov_title">
                        <h4 v-bind:style='{margin:"0"}'><router-link :to="{path:'./detail',query:{name:item._id}}">{{item.name}}</router-link></h4>
                    </div>
                </div>
            </div>
            <div class="rank">
                <ul class="ul_rank">
                    <li v-for="(item,index) in dt9" :key="index">
                        <span class="m1">{{item.kind}}</span>
                        <router-link :to="{path:'./detail',query:{name:item._id}}" class="m2">{{item.name}}</router-link>
                        <span class="m3">{{item.definition}}</span>
                    </li>
                </ul>
            </div>
        </div>
        <hr v-bind:style='{width:"1137px",margin:"0 auto"}'>
        <div class="title">
            <div class="new_m">
                <h3 class="h3">
                    <span>最新综艺</span>
                </h3>
            </div>
            <div class="more">
                <router-link :to="{
                            path:'/movie',
                            query:{kind:'综艺'}
                        }">更多>></router-link>    
            </div>
        </div>
        <div class="con">
            <div class="movie2">
                <div class="mark" v-for="(item,index) in dt7" :key="index">
                    <div class="like">
                        <router-link :to="{path:'./detail',query:{name:item._id}}">
                            <img v-lazy=item.img_url :src=item.img_url :onerror="default_img_url" alt="" v-bind:style='{width:"100%",height:"100%"}'>
                        </router-link>
                        <span class="gold">{{item.douban_score}}</span>
                        <span class="episode">{{item.definition | ellipsis}}</span>
                    </div>
                    <div class="mov_title">
                        <h4 v-bind:style='{margin:"0"}'><router-link :to="{path:'./detail',query:{name:item._id}}">{{item.name}}</router-link></h4>
                    </div>
                </div>
        </div>
        <div class="rank">
            <ul class="ul_rank">
                    <li v-for="(item,index) in dt10" :key="index">
                        <span class="m1">{{item.kind}}</span>
                            <router-link :to="{path:'./detail',query:{name:item._id}}" class="m2">{{item.name}}</router-link>
                        <span class="m3">{{item.definition}}</span>
                    </li>
            </ul>
        </div>
        </div>
        <hr v-bind:style='{width:"1137px",margin:"0 auto"}'>
        <div style="background:rgb(51,51,51);padding-top:30px;height:100px;text-align:center;color:#999999;margin-top:30px">本网站内容收集于互联网，刘震.PY不承担任何由于内容的合法性及健康性所引起的争议和法律责任。<br>
本站永久免费更新最新电影与剧集，欢迎大家使用并推荐朋友。</div>
    </div>
</template>

<script>
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
export default {
    name:'head1',
    filters: {
        ellipsis (value) {
        if (!value) return ''
        if (value.length > 5) {
            return value.slice(0,5) + '...'
        }
        return value
        }
    },
    data() {
        return {
            sort:["电影","欧美电影","日韩电影","港台电影","大陆电影","动漫","日韩剧","港台剧","大陆剧","欧美剧","综艺"],
            //设置属性
            swiperOption:{
                //显示分页
                pagination: {
                    el: '.swiper-pagination',
                    clickable:true
                },
                //切换模式  横屏或者竖屏
                // direction : 'vertical',
                //设置自动播放速度
                autoplay: {
                    disableOnInteraction: false,
                    delay:4000
                },
                //开启无限循环
                loop:false,
                //设置点击箭头
                paginationClickable :true,
                prevButton:'.swiper-button-prev',
                nextButton:'.swiper-button-next',
                //设置同屏显示的数量，默认为1，使用auto是随意的意思。
                slidesPerView:1,
                //开启鼠标滚轮控制Swiper切换。可设置鼠标选项，或true使用默认值。
                mousewheel:true ,
                //默认为false，普通模式：slide滑动时只滑动一格，并自动贴合wrapper，设置为true则变为free模式，slide会根据惯性滑动可能不止一格且不会贴合。
                // freeMode:true
            },
            dt:'',
            dt1:'',
            dt2:'',
            dt3:'',
            dt4:'',
            dt5:'',
            dt6:'',
            dt7:'',
            dt8:'',
            dt9:'',
            dt10:'',
            input_text:'',
            default_img_url:'this.src="'+require('../assets/img/default.jpg')+'"'
        }
    },
    methods: {
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
        data1(){
            this.$http.get(this.$store.state.baseUrl+'/app01/index_recommend_img/?kw=剧')
            .then((res)=>{
                this.dt=res.data
            })
            .catch((res)=>{
                console.log('失败的回调',res)
            })
        },
        data2(){
            this.$http.get(this.$store.state.baseUrl+"/app01/index_recommend_img/?kw=综艺")
            .then((res)=>{
                this.dt1=res.data
            })
            .catch((res)=>{
                console.log('失败的回调',res)
            })
        },
        data3(){
            this.$http.get(this.$store.state.baseUrl+'/app01/index_recommend_img/?kw=动漫')
            .then((res)=>{
                this.dt2=res.data
            })
            .catch((res)=>{
                console.log('失败的回调',res)
            })
        },
        data4(){
            this.$http.get(this.$store.state.baseUrl+'/app01/index_recommend_img/?kw=电影&num=12')
            .then((res)=>{
                this.dt3=res.data
            })
            .catch((res)=>{
                console.log('失败的回调',res)
            })
        },
        data5(){
            this.$http.get(this.$store.state.baseUrl+'/app01/indexrecommend_text/?kind=首页电影&num=10')
            .then((res)=>{
                this.dt4=res.data
            })
            .catch((res)=>{
                console.log('失败的回调',res)
            })
        },
        data6(){
            this.$http.get(this.$store.state.baseUrl+'/app01/index_recommend_img/?kw=剧&num=12')
            .then((res)=>{
                this.dt5=res.data
            })
            .catch((res)=>{
                console.log('失败的回调',res)
            })
        },
        data7(){
            this.$http.get(this.$store.state.baseUrl+'/app01/index_recommend_img/?kw=动漫&num=12')
            .then((res)=>{
                this.dt6=res.data
            })
            .catch((res)=>{
                console.log('失败的回调',res)
            })
        },
        data8(){
            this.$http.get(this.$store.state.baseUrl+'/app01/index_recommend_img/?kw=综艺&num=12')
            .then((res)=>{
                this.dt7=res.data
            })
            .catch((res)=>{
                console.log('失败的回调',res)
            })
        },
        data9(){
            this.$http.get(this.$store.state.baseUrl+'/app01/indexrecommend_text/?kind=首页剧&num=10')
            .then((res)=>{
                this.dt8=res.data
            })
            .catch((res)=>{
                console.log('失败的回调',res)
            })
        },
        data10(){
            this.$http.get(this.$store.state.baseUrl+'/app01/indexrecommend_text/?kind=首页动漫&num=10')
            .then((res)=>{
                this.dt9=res.data
            })
            .catch((res)=>{
                console.log('失败的回调',res)
            })
        },
        data11(){
            this.$http.get(this.$store.state.baseUrl+'/app01/indexrecommend_text/?kind=首页综艺&num=10')
            .then((res)=>{
                this.dt10=res.data
            })
            .catch((res)=>{
                console.log('失败的回调',res)
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
    created(){
        
    },
    mounted() {
        this.data1(),
        this.data2(),
        this.data3(),
        this.data4(),
        this.data5(),
        this.data6(),
        this.data7(),
        this.data8(),
        this.data9(),
        this.data10(),
        this.data11()
    },
    activated(){
        this.input_text=''
    },
    components: {
        swiper,
        swiperSlide
    }
}
</script>

<style scoped>
    @import url("../assets/css/head1.css");
    @import url("../assets/css/font.css");
    @import url("../assets/css/logo.css");
</style>
