import express from 'express';
import { execSync } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const app = express();
const PORT = 3003;

let branchName = 'unknown';
try {
  branchName = execSync('git rev-parse --abbrev-ref HEAD', { encoding: 'utf8' }).trim();
} catch {
  // ignore
}

app.use((req, res, next) => {
  res.setHeader('local-branch-name', branchName);
  next();
});

app.use(express.static(path.join(__dirname, 'src/pages')));

app.listen(PORT, () => {
  console.log(`Content server running at http://localhost:${PORT}`);
});
