<template>
    <div class="search">
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
        <div class="third">
            <div class="third_left_movie" v-if="is_found">
                <div class="re_bo">
                    以下是关于"<span>{{sousuo_text}}</span>"的搜索结果
                </div>
                <div class="one_movie" v-for="(item,index) in canshu" :key="index">
                    <div class="one_movie_all">
                        <router-link to="/detail">
                            <div class="one_movie_pic">
                                <div class="one_movie_img">
                                    <router-link :to="{path:'/detail',query:{name:item._id}}">
                                        <img v-lazy=item.img_url :src=item.img_url :onerror="default_img_url" alt="">
                                    </router-link>
                                </div>
                                <span class="gold_1">{{item.douban_score}}</span>
                                <span class="gaoqing">{{item.definition}}</span>
                            </div>
                        </router-link>
                        <router-link :to="{path:'/detail',query:{name:item._id}}">
                        <span class="title_css">
                        {{item.name}}
                        </span>
                        </router-link>
                    </div>
                </div>
            </div>
            <div v-if="not_found" class="third_left_movie">
                <div class="img_notfound">
                    <img src="../assets/img/404.gif" alt="">
                </div>
                   <div class="movie2">
                    <div class="re_bo">热门推荐</div>
                    <div class="mark" v-for="(item,index) in canshu2" :key="index">
                        <div class="like">
                            <router-link :to="{path:'/detail',query:{name:item._id}}" >
                                <img v-lazy=item.img_url :src=item.img_url :onerror="default_img_url" alt="" v-bind:style='{width:"100%",height:"100%"}'>
                            </router-link>
                            <span class="gold">{{item.douban_score}}</span>
                            <span class="episode">{{item.definition}}</span>
                        </div>
                        <div class="mov_title">
                            <router-link :to="{path:'/detail',query:{name:item._id}}" >{{item.name}}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="block" style="width:1242px;margin:40px auto">
            <el-pagination
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page="currentPage1"
                :page-sizes="[24]"
                :page-size="100"
                layout="total, sizes, prev, pager, next, jumper"
                :total=total_page
                :hide-on-single-page=true
                :background=true>
            </el-pagination>
        </div> 
       <div style="background:rgb(51,51,51);padding-top:30px;height:100px;text-align:center;color:#999999;margin-top:30px">本网站内容收集于互联网，刘震.PY不承担任何由于内容的合法性及健康性所引起的争议和法律责任。<br>
本站永久免费更新最新电影与剧集，欢迎大家使用并推荐朋友。</div>
    </div>           
</template>
<script>
    export default {
        data() {
            return {
                currentPage1: 1,
                sort:["电影","欧美电影","日韩电影","港台电影","大陆电影","动漫","日韩剧","港台剧","大陆剧","欧美剧","综艺"],
                canshu:"",
                total_page:"",
                canshu2:"",
                yea:"",
                is_found:true,
                not_found:false,
                default_img_url:'this.src="'+require('../assets/img/default.jpg')+'"',
                linshi_data:'',
                input_text:'',
                sousuo_text:''
            };
        },
        methods: {
            toTop() {
                let top = document.documentElement.scrollTop || document.body.scrollTop;
                // 实现滚动效果 
                const timeTop = setInterval(() => {
                    document.body.scrollTop = document.documentElement.scrollTop = top -= 50;
                    if (top <= 50) {
                    clearInterval(timeTop);
                    }
                }, 10);
            },
            change(){
                let _this = this;
                document.onkeydown = function(e){
                    let _key = window.event.keyCode;
                    if(_key === 13){
                        _this.input()
                    }
                }
            },
            handleSizeChange(val) {
                console.log(`每页 ${val} 条`);
            },
            handleCurrentChange(val) {
                this.toTop()
                this.currentPage1=val,
                this.canshu=this.linshi_data.slice((val-1)*24,val*24)
            },
            input(){
                this.total_page=''
                console.log(this.input_text)
                this.hanshu(this.input_text)
            },
            hanshu(kw){
                this.sousuo_text=kw
                this.$http.get(this.$store.state.baseUrl+"/app01/search/?kw="+kw)
                .then((res)=>{
                    console.log(res.data)
                    if (res.data!=404){
                        this.is_found=true;
                        this.not_found=false;
                        this.tuijian(res.data[0].kind);
                        if (res.data.length<=24){
                            this.canshu=res.data;
                            console.log(this.canshu[0].kind);
                        }
                        else{
                            this.linshi_data=res.data
                            this.canshu=res.data.slice(0,24)
                            this.total_page=res.data.length
                            console.log(res.data.length,this.total_page)
                        }
                    }
                    else{
                        this.is_found=false;
                        this.not_found=true;
                        this.tuijian()
                    }
                })
                .catch((res)=>{
                    console.log("失败的回调",res)
                })
            },
            tuijian(kind){
                kind=kind||'电影'
                this.$http.get(this.$store.state.baseUrl+"/app01/indexrecommend_text/?kind="+kind)
                .then((res)=>{
                    this.canshu2=res.data.slice(0,6);
                    console.log(this.canshu2)
                })
                .catch((res)=>{
                    console.log("失败的回调",res)
                })
            },
        },
        created(){
            this.hanshu(this.$route.query.search_text)
        }
    }
</script>

<style scoped>
    @import url("../assets/css/search.css");
    @import url("../assets/css/font.css");
    @import url("../assets/css/logo.css");
</style>