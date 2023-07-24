// next.config.js
const withNextra = require('nextra')('nextra-theme-docs', './theme.config.jsx');

module.exports = withNextra({
  // Your other Next.js configuration options go here

  // Define the default meta tags for all pages
  head: () => ({
    title: 'Your Site Title',
    meta: [
      {
        name: 'description',
        content: 'Your default site description goes here',
      },
      // Add other meta tags here if needed
    ],
  }),
});
