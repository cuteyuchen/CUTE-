import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        baseUrl:'http://140.143.207.193',
        default_img_url:'this.src="'+require('../src/assets/img/default.jpg')+'"'
    }
})