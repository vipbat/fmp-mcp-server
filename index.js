#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

// Determine Python command based on platform
const pythonCmd = process.platform === 'win32' ? 'python' : 'python3';

// Path to the server script
const serverPath = path.join(__dirname, 'server.py');

// Check if server.py exists
if (!fs.existsSync(serverPath)) {
  console.error('Error: server.py not found at', serverPath);
  process.exit(1);
}

// Check for FMP API key
if (!process.env.FMP_API_KEY) {
  console.error('Error: FMP_API_KEY environment variable is required');
  console.error('Please set it in your Claude Desktop configuration');
  process.exit(1);
}

console.error('Starting FMP MCP Server...');

// Spawn the Python server with stdio transport
const server = spawn(pythonCmd, [serverPath], {
  stdio: 'inherit',
  env: {
    ...process.env,
    MCP_TRANSPORT: 'stdio'  // Ensure stdio transport
  }
});

// Handle errors
server.on('error', (err) => {
  if (err.code === 'ENOENT') {
    console.error(`Error: ${pythonCmd} not found. Please ensure Python is installed.`);
    console.error('You may need to install Python 3.8 or higher.');
  } else {
    console.error('Failed to start MCP server:', err);
  }
  process.exit(1);
});

// Handle server exit
server.on('exit', (code, signal) => {
  if (code !== null) {
    process.exit(code);
  } else if (signal) {
    console.error(`Server terminated by signal: ${signal}`);
    process.exit(1);
  }
});

// Handle process termination
process.on('SIGINT', () => {
  server.kill('SIGINT');
});

process.on('SIGTERM', () => {
  server.kill('SIGTERM');
});