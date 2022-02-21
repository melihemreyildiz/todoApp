import Vue from 'vue'
import VueRouter from 'vue-router'
import Auth from "@/views/Auth";
import HomePage from "@/views/HomePage";
import AboutView from "@/views/AboutView"
import ToDo from "@/views/ToDo"
import Groups from "@/views/Groups"
import store from "@/store"

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomePage,
        beforeEnter(to, from, next) {
            if (store.getters.isAuthenticated) {
                next()
            } else {
                next("/auth")
            }
        }
    },
    {
        path: '/about',
        name: 'about',
        component: AboutView,
        beforeEnter(to, from, next) {
            if (localStorage.getItem('token')) {
                next()
            } else {
                next("/auth")
            }
        }
    },
    {
        path: '/auth',
        name: 'auth',
        component: Auth,
    },
    {
        path: '/todos',
        name: 'todos',
        component: ToDo,
        beforeEnter(to, from, next) {
            if (localStorage.getItem('token')) {
                next()
            } else {
                next("/auth")
            }
        }
    },
    {
        path: '/groups',
        name: 'groups',
        component: Groups,
        beforeEnter(to, from, next) {
            if (localStorage.getItem('token')) {
                next()
            } else {
                next("/auth")
            }
        }
    },

]

const router = new VueRouter({
    mode: 'history',
    routes
})

// router.beforeEach((to, from, next) => {
//   if (localStorage.getItem('token')) next();
//   else next('/auth');
// });


export default router
