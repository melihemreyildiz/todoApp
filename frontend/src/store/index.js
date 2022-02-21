import Vue from 'vue'
import Vuex from 'vuex'
import router from "../router"
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        token: "",
    },
    getters: {
        isAuthenticated(state){
            return state.token !== ""
        }
    },
    mutations: {
        setToken(state, token) {
            state.token = token
        },
        clearToken(state) {
            state.token = ""
        }
    },
    actions: {
        initAuth({commit, dispatch}) {
            let token = localStorage.getItem("token")
            if (token) {
                axios.defaults.headers.common['Authorization'] = "Bearer " + token
                commit("setToken", token)
                // let expirationDate = localStorage.getItem("expirationDate")
                // let time = new Date().getTime()
                //
                // if (time >= +expirationDate) {
                //     console.log("token süresi geçmiş...")
                //     dispatch("logout")
                // } else {
                //     commit("setToken", token)
                //     let timerSecond = +expirationDate - time
                //     console.log(timerSecond)
                //     dispatch("setTimeoutTimer", timerSecond)
                //     router.push("/")
                // }

            } else {
                router.push("/auth")
                return false
            }
        },
        login({commit, dispatch, state}, authData) {
            let authLink = "/api/authentication/login/"
            return axios.post(
                authLink ,
                {email: authData.email, password: authData.password}
            ).then(response => {
                // console.log(response.data)
                commit("setToken", response.data.access)
                localStorage.setItem("token", response.data.access)

                // localStorage.setItem("expirationDate", new Date().getTime() + +response.data.expiresIn * 1000)
                // // localStorage.setItem("expirationDate", new Date().getTime() + 10000)
                //
                // dispatch("setTimeoutTimer", +response.data.expiresIn * 1000)
                // dispatch("setTimeoutTimer", 10000)
            })
        },
        register({dispatch},authData){
            let authLink = "/api/register/"
            return axios.post(authLink,{email: authData.email,first_name: authData.firstName,
                last_name: authData.lastName,password: authData.password,
                password2:authData.password2
            }).catch( r => {
                console.log(r)
            })
        },
        logout({commit}) {
            commit("clearToken")
            localStorage.removeItem("token")
            // localStorage.removeItem("expirationDate")
            router.replace("/auth")
        },
        setTimeoutTimer({dispatch}, expiresIn) {
            setTimeout(() => {
                dispatch("logout")
            }, expiresIn)
        }

    },
    modules: {}
})
