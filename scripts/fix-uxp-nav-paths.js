const fs = require('fs');
const path = require('path');

const navFiles = ['reference-js.js', 'reference-css.js', 'reference-html.js', 'reference-spectrum.js'];
const baseDir = 'src/pages';

function normalize(s) {
  return s.toLowerCase().replace(/[-_ .]/g, '');
}

function listDir(dir) {
  try { return fs.readdirSync(dir); } catch { return []; }
}

function resolveSegment(currentDir, segment) {
  const entries = listDir(currentDir);
  const segNorm = normalize(segment);

  for (const e of entries) {
    const fullPath = path.join(currentDir, e);
    const stat = fs.statSync(fullPath);
    if (stat.isDirectory() && e === segment) return { name: e, isDir: true };
  }

  for (const e of entries) {
    if (e === segment + '.md') return { name: segment, isDir: false };
  }

  for (const e of entries) {
    const fullPath = path.join(currentDir, e);
    const stat = fs.statSync(fullPath);
    if (stat.isDirectory() && normalize(e) === segNorm) return { name: e, isDir: true };
  }

  for (const e of entries) {
    if (e.endsWith('.md') && normalize(e.replace(/\.md$/, '')) === segNorm) {
      return { name: e.replace(/\.md$/, ''), isDir: false };
    }
  }

  return null;
}

function fixPath(origPath) {
  const segments = origPath.split('/').filter(Boolean);
  const resolved = [];
  let currentDir = baseDir;

  for (const seg of segments) {
    const result = resolveSegment(currentDir, seg);
    if (result) {
      resolved.push(result.name);
      if (result.isDir) currentDir = path.join(currentDir, result.name);
    } else {
      resolved.push(seg);
      currentDir = path.join(currentDir, seg);
      console.error(`  WARNING: could not resolve "${seg}" in ${currentDir}`);
    }
  }

  const lastSeg = segments[segments.length - 1];
  const lastParentDir = path.join(baseDir, ...resolved.slice(0, -1));
  const lastResult = resolveSegment(lastParentDir, lastSeg);

  let newPath = '/' + resolved.join('/');
  if (lastResult && lastResult.isDir) newPath += '/';

  return newPath;
}

let totalFixed = 0;

for (const file of navFiles) {
  let content = fs.readFileSync(file, 'utf8');
  const pathRegex = /"path":\s*"([^"]+)"/g;
  let match;
  const replacements = [];
  const seen = new Set();

  while ((match = pathRegex.exec(content)) !== null) {
    const oldPath = match[1];
    if (seen.has(oldPath)) continue;
    seen.add(oldPath);
    const newPath = fixPath(oldPath);
    if (oldPath !== newPath) replacements.push({ old: oldPath, new: newPath });
  }

  for (const r of replacements) {
    content = content.split('"' + r.old + '"').join('"' + r.new + '"');
    totalFixed++;
  }

  fs.writeFileSync(file, content);
  console.log(`${file}: ${replacements.length} paths fixed`);
}

console.log(`\nTotal paths fixed: ${totalFixed}`);
