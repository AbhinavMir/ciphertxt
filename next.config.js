const withNextra = require('nextra')({
  theme: 'nextra-theme-docs',
  themeConfig: './theme.config.jsx',
  latex: true, // Add the 'latex' option here
});

module.exports = withNextra();
