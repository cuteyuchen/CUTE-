<template>
    <div class="movie">
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
                    <li v-for="(item, index) in sort_head" :key="index" class="sort_rou">
                        <span @click="to_other(item)" class="rou" :class="{rou_select:sort_index===item}">
                             {{item}} 
                        </span>
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
        <div class="index_sort">
            <router-link to="/head1">首页</router-link>
            <span>>></span>
            <router-link to="/movie">{{kind}}</router-link>
        </div>
        <div class="second">
            <div class="year_sort">
                <span class="sort_span">年代：</span>
                <span @click="update1($event,item)" class="year__1" v-for="(item, index1) in year_1" :key="index1" :class="{year__1_select:year_index==item}">{{item}}</span>
            </div> 
            <div class="p_sort">
                <span class="sort_span">排序：</span>
                <span @click="show_date('-show_date',0)" class="p_sort_all" :class="{year__1_select:p_sort===0}">最近更新</span>
                <span @click="show_date('-douban_score',1)" class="p_sort_all" :class="{year__1_select:p_sort===1}">评分</span>
            </div>
        </div>
        <div class="third">
            <div class="one_movie" v-for="(item,index) in canshu" :key="index">
                <div class="one_movie_pic">
                    <div class="one_movie_img">
                        <router-link :to="{path:'/detail',query:{name:item._id}}">
                            <img v-lazy=item.img_url :src=item.img_url :onerror="default_img_url" alt="">
                        </router-link>
                    </div>
                    <span class="gold_1">{{item.douban_score}}</span>
                    <span class="gaoqing">{{item.definition}}</span>
                </div>
                <router-link :to="{path:'/detail',query:{name:item._id}}" class="one_movie_name">{{item.name}}</router-link>
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
                sort_head:["电影","欧美电影","日韩电影","港台电影","大陆电影","动漫","日韩剧","港台剧","大陆剧","欧美剧","综艺"],
                canshu:"",
                total_page:"",
                canshu2:"",
                yea:"",
                year_1:["2019","2018","2017","2016","2015","2014","2013","2012","2011","2010","2009"],
                kind:'',
                sort:'',
                sort_index:'',
                year_index:'',
                p_sort:'',
                input_text:'',
                default_img_url:'this.src="'+require('../assets/img/default.jpg')+'"'
            };
        },
        methods: {
            toTop() {
                let top = document.documentElement.scrollTop || document.body.scrollTop;
                // 实现滚动效果 
                const timeTop = setInterval(() => {
                    document.body.scrollTop = document.documentElement.scrollTop = top -= 50;
                    if (top <= 200) {
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
            show_date(sort,index){
                console.log(this.currentPage1)
                this.sort=sort
                this.p_sort=index
                console.log(this.p_sort)
                if (this.yea==''){
                    this.$http.get(this.$store.state.baseUrl+"/app01/querymovie/?page=1&kind="+this.kind+"&sort="+sort)
                        .then((res)=>{
                            this.canshu=res.data;
                            // console.log(this.canshu)
                        })
                        .catch((res)=>{
                            console.log("失败的回调",res)
                        })
                }
                else{
                    this.$http.get(this.$store.state.baseUrl+"/app01/querymovie/?page=1&kind="+this.kind+"&sort="+sort+"&year="+this.yea)
                        .then((res)=>{
                            this.canshu=res.data;
                            // console.log(this.canshu)
                        })
                        .catch((res)=>{
                            console.log("失败的回调",res)
                        })
                }
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
            kind_text(){
                this.kind=this.$route.query.kind;
                this.sort_index=this.$route.query.kind
            },
            to_other(kind){
                this.kind=kind,
                this.hanshu(kind),
                this.yeshu(kind),
                this.tuijian(kind),
                this.sort_index=kind,
                this.sort_inde='',
                this.year_index='',
                this.p_sort='',
                this.toTop()
            },
            handleSizeChange(val) {
                console.log(`每页 ${val} 条`);
            },
            handleCurrentChange(val) {
                this.currentPage1=val
                this.toTop()
                console.log(`当前页: ${val}`);
                    if(this.yea=='' &this.sort==''){
                    this.$http.get(this.$store.state.baseUrl+"/app01/querymovie/?page="+val+'&kind='+this.kind)
                    .then((res)=>{
                        this.canshu=res.data;
                        // console.log(this.canshu)
                    })
                    .catch((res)=>{
                        console.log("失败的回调",res)
                    })
                }
                else if(this.yea!=''&this.sort==''){
                    this.$http.get(this.$store.state.baseUrl+"/app01/querymovie/?page="+val+'&kind='+this.kind+'&year='+this.yea)
                    .then((res)=>{
                        this.canshu=res.data;
                        // console.log(this.canshu)
                    })
                    .catch((res)=>{
                        console.log("失败的回调",res)
                    })
                }
                else if(this.sort!=''&this.yea==''){
                    this.$http.get(this.$store.state.baseUrl+"/app01/querymovie/?page="+val+'&kind='+this.kind+'&sort='+this.sort)
                    .then((res)=>{
                        this.canshu=res.data;
                        // console.log(this.canshu)
                    })
                    .catch((res)=>{
                        console.log("失败的回调",res)
                    })
                }
                else if(this.sort!=''&this.yea!=''){
                    this.$http.get(this.$store.state.baseUrl+"/app01/querymovie/?page="+val+"&kind="+this.kind+"&sort="+this.sort+"&year="+this.yea)
                    .then((res)=>{
                        this.canshu=res.data;
                        // console.log(this.canshu)
                    })
                    .catch((res)=>{
                        console.log("失败的回调",res)
                    })
                }
            },
            hanshu(kind){
                this.$http.get(this.$store.state.baseUrl+"/app01/querymovie/?page=1&kind="+kind)
                .then((res)=>{
                    this.canshu=res.data;
                    // console.log(this.canshu)
                })
                .catch((res)=>{
                    console.log("失败的回调",res)
                })
            },
            yeshu(kind){
                this.$http.get(this.$store.state.baseUrl+"/app01/get_pages/?kind="+kind)
                .then((res)=>{
                    this.total_page=res.data;
                    // console.log(this.total_page)
                })
                .catch((res)=>{
                    console.log("失败的回调",res)
                })
            },
            tuijian(kind){
                this.$http.get(this.$store.state.baseUrl+"/app01/indexrecommend_text/?kind="+kind)
                .then((res)=>{
                    this.canshu2=res.data;
                    // console.log(this.canshu2)
                })
                .catch((res)=>{
                    console.log("失败的回调",res)
                })
            },
            update1(e,index){
                this.year_index=index
                this.yea=e.target.innerHTML
                console.log(this.yea)
                if (this.sort==''){
                    this.$http.get(this.$store.state.baseUrl+"/app01/querymovie/?kind="+this.kind+"&year="+this.yea)
                    .then((res)=>{
                        this.canshu=res.data;
                        console.log(this.canshu)
                        this.$http.get(this.$store.state.baseUrl+"/app01/get_pages/?kind="+this.kind+"&year="+this.yea)
                        .then((res)=>{
                            this.total_page=res.data;
                            console.log(this.total_page)
                        })
                        .catch((res)=>{
                            console.log("失败的回调",res)
                        })
                    })
                    .catch((res)=>{
                        console.log('失败的回调',res)
                    })
                }
                else{
                    this.$http.get(this.$store.state.baseUrl+"/app01/querymovie/?kind="+this.kind+"&year="+this.yea+'&sort='+this.sort)
                    .then((res)=>{
                        this.canshu=res.data;
                        console.log(this.canshu)
                        this.$http.get(this.$store.state.baseUrl+"/app01/get_pages/?kind="+this.kind+"&year="+this.yea)
                        .then((res)=>{
                            this.total_page=res.data;
                            console.log(this.total_page)
                        })
                        .catch((res)=>{
                            console.log("失败的回调",res)
                        })
                    })
                    .catch((res)=>{
                        console.log('失败的回调',res)
                    })
                }
            }
        },
        created() {
            this.kind_text()
        },
        mounted(){
            this.hanshu(this.kind),
            this.yeshu(this.kind),
            this.tuijian(this.kind)
        }
    }
</script>

<style scoped>
    @import url("../assets/css/movie.css");
    @import url("../assets/css/font.css");
    @import url("../assets/css/logo.css");
</style>