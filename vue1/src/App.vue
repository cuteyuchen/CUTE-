<template>
  <div id="app">
   <keep-alive exclude="search_bar_input">
        <router-view v-if="$route.meta.keepAlive"></router-view>
    </keep-alive>
    <router-view v-if="!$route.meta.keepAlive"></router-view>
  </div>
</template>

<script>
import head1 from "./components/head1"
export default {
  name: 'App',
  components: {
    head1
  },
  methods:{
  }
}
</script>

<style>
*{
  margin: 0;
  padding: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  /* color: #2c3e50; */
}
a{
  text-decoration: none;
}
li{
  list-style: none;
}
input{
  outline: none
}
</style>
