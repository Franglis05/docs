import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Solop",
  base: '/',
  description: "Documentación oficial de Solop ERP",
  lang: 'es-ES',
  lastUpdated: true,
  head: [['link', { rel: 'icon', href: '/favicon.ico' }]],
  themeConfig: {
    search: {
      provider: 'local'
    },
    logo: '/logo_alone.png',
    // logoLink: 'https://solopsoftware.com/es/inicio/',
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Inicio', link: 'https://solopsoftware.com/es/inicio/' },
      { text: 'Reglas Básicas', link: '/basic-rules' },
      { text: 'Funcionalidades', link: '/master-data' },
    ],



    socialLinks: [
      { icon: 'github', link: 'https://github.com/solop-develop/docs' }
    ],
    footer: {
      copyright: 'Copyright © 2024-present Solop Software'
    }
  }
})
