import { createApp } from 'vue'
import VueGtag from "vue-gtag";
import App from './App.vue'
import router from './router'

import './index.css'

const app = createApp(App)

app.use(router)

app.use(
    VueGtag,
    {
        config: { id: "G-30YWL18JNW" }
    },
    router
);

app.mount('#app')
