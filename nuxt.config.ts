// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  quiet: false,
  app: {
    head: {
      title: 'Habito',
      meta: [
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content: 'A simple portal to track your habits and todo.'
        }
      ]
    }
  },
  css: ['@fortawesome/fontawesome-free/css/all.css'],
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', '@nuxtjs/supabase'],
  supabase: {
    redirectOptions: {
      login: '/login',
      callback: '/confirm',
      exclude: ['/*'],
    },
  },
})
