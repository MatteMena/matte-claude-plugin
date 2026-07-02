import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'MatteMena Docs',
  tagline: 'Manage Meta, TikTok, Google Ads & more with Claude AI',
  favicon: 'img/favicon.png',

  stylesheets: [
    {
      href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap',
      type: 'text/css',
    },
  ],

  future: {
    v4: true,
  },

  url: 'https://docs.nerve.mattemena.com',
  baseUrl: '/',

  organizationName: 'MatteMena',
  projectName: 'matte-claude-plugin',

  onBrokenLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: 'docs',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/og-card.png',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    announcementBar: {
      id: 'plugin-announcement',
      content:
        '🚀 MatteMena is now available in the Claude Code plugin directory — <a href="/docs/installation">Install now</a>',
      backgroundColor: '#22299c',
      textColor: '#ffffff',
      isCloseable: true,
    },
    navbar: {
      title: '',
      style: 'dark',
      logo: {
        alt: 'MatteMena',
        src: 'img/logo-white.svg',
        srcDark: 'img/logo-white.svg',
        height: 28,
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'mainSidebar',
          position: 'left',
          label: 'Docs',
        },
        {
          to: '/docs/tools/overview',
          label: 'Tool Reference',
          position: 'left',
        },
        {
          href: 'https://nerve.mattemena.com',
          label: 'Sign Up',
          position: 'right',
        },
        {
          href: 'https://github.com/MatteMena/matte-claude-plugin',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Get Started',
          items: [
            { label: 'Introduction', to: '/docs/intro' },
            { label: 'Installation', to: '/docs/installation' },
            { label: 'Authentication', to: '/docs/authentication' },
          ],
        },
        {
          title: 'Platforms',
          items: [
            { label: 'Meta (Facebook/Instagram)', to: '/docs/platforms/meta' },
            { label: 'TikTok Ads', to: '/docs/platforms/tiktok' },
            { label: 'Google Ads', to: '/docs/platforms/google-ads' },
            { label: 'Google Analytics (GA4)', to: '/docs/platforms/ga4' },
            { label: 'Google Sheets', to: '/docs/platforms/google-sheets' },
            { label: 'HubSpot CRM', to: '/docs/platforms/hubspot' },
          ],
        },
        {
          title: 'Resources',
          items: [
            { label: 'Tool Reference', to: '/docs/tools/overview' },
            { label: 'Privacy Policy', to: '/docs/privacy-policy' },
            { label: 'hello@mattemena.com', href: 'mailto:hello@mattemena.com' },
            { label: 'nerve.mattemena.com', href: 'https://nerve.mattemena.com' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} MatteMena. All rights reserved.`,

    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
