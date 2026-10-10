'use strict';
const http = require('node:http');
const os = require('node:os');
const fs = require('node:fs');
const path = require('node:path');

const port = 8766;
const server = http.createServer((request, response) => {
  if (request.url !== '/' && request.url !== '/index.html') {
    response.writeHead(404); response.end('Not found'); return;
  }
  response.writeHead(200, {
    'Content-Type': 'text/html; charset=utf-8',
    'Cache-Control': 'no-store',
    'X-Content-Type-Options': 'nosniff'
  });
  response.end(fs.readFileSync(path.join(__dirname, 'index.html')));
});
server.listen(port, '0.0.0.0', () => {
  console.log('\nOpen this address on your phone while both devices use the same Wi-Fi:');
  for (const entries of Object.values(os.networkInterfaces())) {
    for (const item of entries || []) {
      if (item.family === 'IPv4' && !item.internal) console.log(`http://${item.address}:${port}`);
    }
  }
  console.log('\nKeep this window open. Press Ctrl+C to stop the server.');
});
server.on('error', error => { console.error('Could not start the server:', error.message); process.exitCode = 1; });
