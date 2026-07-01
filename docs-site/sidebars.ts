import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  mainSidebar: [
    'intro',
    'installation',
    'authentication',
    {
      type: 'category',
      label: 'Platform Guides',
      collapsed: false,
      items: [
        'platforms/meta',
        'platforms/tiktok',
        'platforms/google-ads',
        'platforms/ga4',
        'platforms/snapchat',
        'platforms/google-sheets',
        'platforms/hubspot',
      ],
    },
    {
      type: 'category',
      label: 'Tool Reference',
      collapsed: true,
      items: [
        'tools/overview',
        'tools/meta',
        'tools/tiktok',
        'tools/google-ads',
        'tools/ga4',
        'tools/snapchat',
        'tools/google-sheets',
        'tools/hubspot',
        'tools/discovery',
      ],
    },
    'faq',
    'privacy-policy',
  ],
};

export default sidebars;
