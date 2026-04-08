const ctxJs = require.context('../src/pages/uxp-api/reference-js', true, /\.md$/);
const ctxCss = require.context('../src/pages/uxp-api/reference-css', true, /\.md$/);
const ctxHtml = require.context('../src/pages/uxp-api/reference-html', true, /\.md$/);
const ctxSpectrum = require.context('../src/pages/uxp-api/reference-spectrum', true, /\.md$/);

function loadAll(ctx) {
  ctx.keys().forEach((key) => ctx(key));
}

loadAll(ctxJs);
loadAll(ctxCss);
loadAll(ctxHtml);
loadAll(ctxSpectrum);
