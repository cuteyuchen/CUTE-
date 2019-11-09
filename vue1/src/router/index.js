import Vue from 'vue'
import Router from 'vue-router'
import head1 from "@/components/head1"
import movie from "@/components/movie"
import mp4 from "@/components/mp4"
import detail from "@/components/detail"
import search from "@/components/search"
Vue.use(Router)

export default new Router({
  routes: [
    {
      path:"*",
      redirect:"/head1"      
    },
    {
      path: '/head1',
      name: 'head1',
      component: head1,
      meta:{
        keepAlive:true
      }
    },
    {
    	path: '/movie',
      name: 'movie',
      component: movie
    },
    {
    	path: '/mp4',
      name: 'mp4',
      component: mp4
    },
    {
    	path: '/detail',
      name: 'detail',
      component: detail
    },
    {
    	path: '/search',
      name: 'search',
      component: search
    },

  ]
})
