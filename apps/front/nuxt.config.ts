// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    modules: [['@nuxtjs/google-fonts', {
        families: {
            'Open+Sans': [400, 600, 700],
        }
    }], ],
    devtools: {enabled: true},
    css: [
        '@/assets/scss/main.scss'
    ],
    vite: {
        css: {
            preprocessorOptions: {
                scss: {
                    additionalData: '@import "@/assets/scss/_colors.scss";'
                }
            }
        }
    }
})