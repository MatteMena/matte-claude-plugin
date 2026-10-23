import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  mainSidebar: [
    'intro',
    'installation',
    'authentication',
    {
      type: 'category',
      label: 'Help Center',
      collapsed: false,
      link: {type: 'doc', id: 'help/index'},
      items: [
        {
          type: 'category',
          label: 'Getting Started',
          items: [
            'help/getting-started/sign-up',
            'help/getting-started/create-workspace',
            'help/getting-started/first-prompt',
          ],
        },
        {
          type: 'category',
          label: 'Accounts',
          items: [
            'help/accounts/connect-accounts',
            'help/accounts/choosing-ad-accounts',
          ],
        },
        {
          type: 'category',
          label: 'Workspace',
          items: ['help/workspace/members-and-roles'],
        },
        {
          type: 'category',
          label: 'AI Agents',
          items: [
            'help/ai-agents/nerve-ai-chat',
            'help/ai-agents/workflows',
            'help/ai-agents/running-workflows',
            'help/ai-agents/scheduling-workflows',
            'help/ai-agents/workflow-templates',
          ],
        },
        {
          type: 'category',
          label: 'Analytics',
          items: [
            'help/analytics/advertiser-groups',
            'help/analytics/analytics-dashboard',
          ],
        },
        {
          type: 'category',
          label: 'Planning',
          items: [
            'help/planning/prompt-library',
            'help/planning/media-planner',
          ],
        },
        {
          type: 'category',
          label: 'Connect to AI',
          items: [
            'help/connect-ai/claude',
            'help/connect-ai/chatgpt',
            'help/connect-ai/how-tools-work',
          ],
        },
        {
          type: 'category',
          label: 'Billing',
          items: [
            'help/billing/free-trial',
            'help/billing/plans-and-pricing',
            'help/billing/subscribe-and-payment-methods',
            'help/billing/credits-and-top-ups',
            'help/billing/invoices-cancel-and-payment-failure',
          ],
        },
        'help/troubleshooting',
      ],
    },
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
