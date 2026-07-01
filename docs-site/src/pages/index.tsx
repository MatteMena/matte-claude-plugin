import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from './index.module.css';

const platforms = [
  { name: 'Meta Ads', desc: 'Facebook & Instagram campaigns, creatives, audiences, pixels, and insights', icon: '/img/platforms/meta.svg', href: '/docs/platforms/meta' },
  { name: 'TikTok Ads', desc: 'Campaigns, ad groups, creatives, audiences, pixels, and performance metrics', icon: '/img/platforms/tiktok.svg', href: '/docs/platforms/tiktok' },
  { name: 'Google Ads', desc: 'Campaigns, keywords, bidding strategies, PMax, and performance insights', icon: '/img/platforms/google-ads.svg', href: '/docs/platforms/google-ads' },
  { name: 'Google Analytics', desc: 'Traffic, channels, conversions, funnels, e-commerce, and attribution', icon: '/img/platforms/ga4.svg', href: '/docs/platforms/ga4' },
  { name: 'Snapchat Ads', desc: 'Campaigns, ad squads, creatives, audiences, and stats', icon: '/img/platforms/snapchat.svg', href: '/docs/platforms/snapchat' },
  { name: 'Google Sheets', desc: 'Read and write spreadsheet data directly from Claude', icon: '/img/platforms/google-sheets.svg', href: '/docs/platforms/google-sheets' },
  { name: 'HubSpot CRM', desc: 'Contacts, companies, deals, and tickets', icon: '/img/platforms/hubspot.svg', href: '/docs/platforms/hubspot' },
];

function Hero() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={`hero hero--primary ${styles.heroBanner}`}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link className="button button--secondary button--lg" to="/docs/installation">
            Install the Plugin
          </Link>
          <Link className="button button--outline button--secondary button--lg" to="/docs/intro" style={{marginLeft: '1rem'}}>
            Read the Docs
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  return (
    <Layout
      title="MatteMena Docs"
      description="Connect Claude to Meta, TikTok, Google Ads, GA4, Snapchat, Google Sheets, and HubSpot.">
      <Hero />
      <main>
        <section style={{ padding: '4rem 0' }}>
          <div className="container">
            <div className="text--center" style={{ marginBottom: '3rem' }}>
              <Heading as="h2">Supported Platforms</Heading>
              <p style={{ fontSize: '1.1rem', color: 'var(--ifm-color-content-secondary)' }}>
                Connect once, then manage all your ad platforms through natural language with Claude.
              </p>
            </div>
            <div className="row">
              {platforms.map(({ name, desc, icon, href }) => (
                <div key={name} className="col col--4" style={{ marginBottom: '1.5rem' }}>
                  <Link to={href} style={{ textDecoration: 'none', color: 'inherit' }}>
                    <div className="card shadow--sm" style={{ height: '100%', padding: '1.5rem', transition: 'box-shadow 0.2s', cursor: 'pointer' }}>
                      <img src={icon} alt={name} style={{ width: 40, height: 40, marginBottom: '0.75rem', borderRadius: 8 }} />
                      <Heading as="h3" style={{ fontSize: '1.05rem', marginBottom: '0.4rem' }}>{name}</Heading>
                      <p style={{ fontSize: '0.875rem', color: 'var(--ifm-color-content-secondary)', margin: 0, lineHeight: 1.5 }}>{desc}</p>
                    </div>
                  </Link>
                </div>
              ))}
            </div>
            <div className="text--center" style={{ marginTop: '3rem' }}>
              <Link className="button button--primary button--lg" to="/docs/intro">
                Get Started
              </Link>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
