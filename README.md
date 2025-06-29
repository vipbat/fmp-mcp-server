# FMP MCP Server

An MCP (Model Context Protocol) server that provides Financial Modeling Prep API integration for Claude Desktop. Built specifically for Investment Banking Analysts and M&A professionals to perform sophisticated financial analysis using natural language.

## Features

- 🏦 **Company Profiles** - Get detailed company information including sector, industry, and descriptions
- 📊 **Financial Statements** - Access income statements, balance sheets, and cash flow statements
- 📈 **Financial Ratios** - Retrieve key metrics like P/E ratio, ROE, ROA, and more
- 💰 **Enterprise Value** - Get enterprise value calculations and multiples
- 🔍 **Company Search** - Search for companies by name to find ticker symbols
- 📑 **M&A Analysis** - Perform comparable company analysis and sector valuations

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- Claude Desktop application
- FMP API key (get one at [financialmodelingprep.com](https://financialmodelingprep.com/developer))

## Installation

1. Install the package globally:
```bash
npm install -g @vipbat/fmp-mcp-server
```

2. Install Python dependencies:
```bash
pip install mcp fastmcp httpx
```

## Configuration

Add the server to your Claude Desktop configuration:

### Windows
Edit `%APPDATA%\Claude\claude_desktop_config.json`

### macOS
Edit `~/Library/Application Support/Claude/claude_desktop_config.json`

Add the following to the `mcpServers` section:

```json
{
  "mcpServers": {
    "fmp": {
      "command": "npx",
      "args": ["@vipbat/fmp-mcp-server"],
      "env": {
        "FMP_API_KEY": "your-fmp-api-key-here"
      }
    }
  }
}
```

## Usage

Once configured, restart Claude Desktop. You can then ask Claude to:

- "What's Apple's current P/E ratio?"
- "Show me Microsoft's income statements for the last 3 years"
- "Compare the EV/EBITDA multiples of major tech companies"
- "Analyze if Company X is undervalued compared to its sector peers"
- "What's the enterprise value of Tesla?"
- "Would AMD acquiring Marvell make sense?"
- "Estimate pro-forma Debt/EBITDA for Shopify acquiring Pinterest"
- "Estimate synergies if Twilio acquires Freshworks"
- "Retrieve the latest Enterprise Value and EBITDA for AppFolio and use it to calculate the current EV/EBITDA multiple manually. Then comment if it looks expensive or cheap versus historical averages"
- "Identify two midcap companies in the consumer discretionary sector that could be attractive M&A targets based on healthy EBITDA margins and manageable debt levels"
- "Estimate the post-acquisition debt/EBITDA ratio if Chewy (CHWY) were to acquire Five Below (FIVE) with a $2 billion cash+debt funded deal"
- "Assess whether a potential acquisition of Zynex (ZYXI) by Axon Enterprise (AXON) would make strategic sense based on sector overlap, size compatibility, and financial strength."

## Available Tools

### `get_company_profile`
Fetches comprehensive company information including sector, industry, market cap, and description.

### `get_income_statements`
Retrieves income statements with revenue, expenses, and profit metrics.
- Parameters: `ticker` (required), `limit` (optional, default: 4), `period` (optional, default: "annual")

### `get_balance_sheets`
Gets balance sheet data including assets, liabilities, and equity.
- Parameters: `ticker` (required), `limit` (optional, default: 4)

### `get_cash_flow_statements`
Accesses cash flow statements showing operating, investing, and financing activities.
- Parameters: `ticker` (required), `limit` (optional, default: 4)

### `get_ratios`
Retrieves financial ratios including P/E, P/B, ROE, ROA, and more.
- Parameters: `ticker` (required)

### `get_enterprise_value`
Gets enterprise value calculations and related metrics.
- Parameters: `ticker` (required), `limit` (optional, default: 4)

### `search_companies_by_name`
Searches for companies by name to find ticker symbols.
- Parameters: `query` (required)

## Example Use Cases

### M&A Analysis
"Analyze whether Salesforce's acquisition of Slack was overvalued based on comparable SaaS company multiples"

### Sector Comparison
"Compare the median EV/EBITDA ratios in the cybersecurity sector and identify which companies are trading below sector median"

### Financial Health Check
"Evaluate Microsoft's financial health using key ratios and cash flow trends"

## Troubleshooting

### "FMP_API_KEY environment variable is not set"
Make sure you've added your FMP API key to the Claude Desktop configuration file.

### "Python not found"
Ensure Python 3.8+ is installed and available in your system PATH.

### Server fails to start
Check that all Python dependencies are installed:
```bash
pip install mcp fastmcp httpx
```

## Contributing

Issues and pull requests are welcome at [github.com/vipbat/fmp-mcp-server](https://github.com/vipbat/fmp-mcp-server)

## License

MIT License - see LICENSE file for details

## Acknowledgments

Built for the MCP (Model Context Protocol) ecosystem by Anthropic.