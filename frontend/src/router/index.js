import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/animes',
        name: 'animes',
        component: () => import(/* webpackChunkName: "anime" */ '../views/AnimeView.vue')
    },
    {
        path: '/anime/:slug',
        name: 'anime',
        component: () => import(/* webpackChunkName: "anime" */ '../views/AnimeDetalleView.vue')
    }
]

const router = new VueRouter({
    routes
})

export default router
