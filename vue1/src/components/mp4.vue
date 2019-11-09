<template>
    <div class='mp4'>
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
        <div class="first">
            <div class="first1">
                <a href=""><span>首页</span></a>
                &nbsp;&nbsp;>>&nbsp;&nbsp;
                <a href=""><span>{{m_d.kind}}</span></a>
                &nbsp;&nbsp;>>&nbsp;&nbsp;
                <a href=""><span>{{m_d.name}}</span></a>
            </div>
        </div>
        <div class="totals">
            <div class="run">
                <h1>
                    {{m_d.name}}
                    <small>
                        ({{m_d.years}})
                    </small>
                </h1>
                <div class="moving">
                    <iframe height=100% width=100% :src=iframe_url frameborder=0 ></iframe>
                </div>
                <div>
                    <div class="first_1">播放列表</div>
                    <hr style="width:100%">
                    <div class="first_2" v-for="(value,key, index1) in m_d.m3u8_online" :key="index1">
                        <a @click.prevent="play_movie(value)" style="cursor: pointer;">{{key}}
                        </a>
                    </div>
                </div>
            </div>
            <div class="movie2">
                 <div class="re_bo">相关热播</div>
                <div class="mark" v-for="(item,index) in like" :key="index">
                    <div class="like">
                        <router-link :to="{path:'/detail',query:{name:item._id}}">
                            <img v-lazy=item.img_url :src=item.img_url alt="" v-bind:style='{width:"100%",height:"100%"}'>
                        </router-link>
                        <span class="gold">{{item.douban_score}}</span>
                        <span class="episode">{{item.definition}}</span>
                    </div>
                    <div class="mov_title">
                        <router-link :to="{path:'/detail',query:{name:'item._id'}}">{{item.name}}</router-link>
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
    data() {
        return {
            m_d:"",
            like:"",
            iframe_url:'',
            sort:["电影","欧美电影","日韩电影","港台电影","大陆电影","动漫","日韩剧","港台剧","大陆剧","欧美剧","综艺"],
        }
    },
    methods: {
        change(){
            let _this = this;
            document.onkeydown = function(e){
                let _key = window.event.keyCode;
                if(_key === 13){
                    _this.input()
                }
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
        play_movie(value){
            document.body.scrollTop = document.documentElement.scrollTop = 160;
            this.iframe_url=value
        },
        get_movie_detail(){
            document.body.scrollTop = document.documentElement.scrollTop = 0;
            this.iframe_url=this.$route.query.iframe_url
            this.$http.get(this.$store.state.baseUrl+'/app01/one_movie/?name='+this.$route.query.name)
            .then((res)=>{
                this.m_d=res.data;
                console.log(res.data)
                this.$http.get(this.$store.state.baseUrl+"/app01/indexrecommend_text/?kind="+res.data.kind)
                .then((res1)=>{
                    this.like=res1.data.slice(0,6);
                    console.log(res1.data)
                })
                .catch((res1)=>{
                    console.log("失败的回调111",res1)
                })
            })
            .catch((res)=>{
                console.log('失败的回调222',res)
            })
        },
    },
     mounted(){
            this.get_movie_detail()
        }
}
</script>

<style scoped>
@import url("../assets/css/font.css");
@import url("../assets/css/mp4.css");
@import url("../assets/css/logo.css");
</style>
