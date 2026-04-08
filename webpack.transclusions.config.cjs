const path = require('path');

module.exports = {
  mode: 'production',
  entry: './scripts/uxp-transclusions-context.js',
  output: {
    path: path.resolve(__dirname, '.uxp-webpack-cache'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.md$/,
        use: [
          {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-react'],
            },
          },
          '@mdx-js/loader',
          path.resolve(__dirname, 'scripts/strip-frontmatter-loader.cjs'),
        ],
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.md'],
  },
  stats: 'errors-warnings',
};
