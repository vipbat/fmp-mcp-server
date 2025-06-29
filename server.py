# server.py

import os
import asyncio
import httpx
from mcp.server.fastmcp import FastMCP

# Load FMP API key from environment
FMP_API_KEY = os.getenv("FMP_API_KEY")
if not FMP_API_KEY:
    raise ValueError("FMP_API_KEY environment variable is not set!")

BASE_URL = "https://financialmodelingprep.com/api/v3"

# Initialize FastMCP server instance
mcp = FastMCP("FMP Financial Data MCP")

# Manual tool registry for HTTP wrapper
tools_registry = {}

# Create a reusable HTTPX AsyncClient
client = httpx.AsyncClient(timeout=60.0)

async def fetch_fmp(endpoint: str, retries: int = 2) -> dict:
    if "?" in endpoint:
        url = f"{BASE_URL}/{endpoint}&apikey={FMP_API_KEY}"
    else:
        url = f"{BASE_URL}/{endpoint}?apikey={FMP_API_KEY}"
    
    for attempt in range(retries + 1):
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            if attempt == retries:
                return {"error": str(e)}
            await asyncio.sleep(1)  # wait 1 second before retry


@mcp.tool()
async def get_income_statements(ticker: str, limit: int = 4, period: str = "annual") -> dict:
    """Fetch latest income statements for a company."""
    endpoint = f"income-statement/{ticker}?period={period}&limit={limit}"
    result = await fetch_fmp(endpoint)
    return result

tools_registry["get_income_statements"] = get_income_statements

@mcp.tool()
async def get_balance_sheets(ticker: str, limit: int = 4) -> dict:
    """Fetch latest balance sheets for a company."""
    return await fetch_fmp(f"balance-sheet-statement/{ticker}?limit={limit}")

tools_registry["get_balance_sheets"] = get_balance_sheets

@mcp.tool()
async def get_cash_flow_statements(ticker: str, limit: int = 4) -> dict:
    """Fetch latest cash flow statements for a company."""
    return await fetch_fmp(f"cash-flow-statement/{ticker}?limit={limit}")

tools_registry["get_cash_flow_statements"] = get_cash_flow_statements

@mcp.tool()
async def get_company_profile(ticker: str) -> dict:
    """Fetch company profile, sector, industry, description, etc."""
    return await fetch_fmp(f"profile/{ticker}")

tools_registry["get_company_profile"] = get_company_profile

@mcp.tool()
async def get_ratios(ticker: str) -> dict:
    """Fetch financial ratios for a company (e.g., PE ratio, ROE)."""
    return await fetch_fmp(f"ratios/{ticker}")

tools_registry["get_ratios"] = get_ratios

@mcp.tool()
async def get_enterprise_value(ticker: str, limit: int = 4) -> dict:
    """Fetch enterprise value metrics for a company."""
    return await fetch_fmp(f"enterprise-values/{ticker}?limit={limit}")

tools_registry["get_enterprise_value"] = get_enterprise_value

@mcp.tool()
async def search_companies_by_name(query: str) -> dict:
    """Search companies by name on NASDAQ exchange."""
    return await fetch_fmp(f"search?query={query}&limit=10&exchange=NASDAQ")

tools_registry["search_companies_by_name"] = search_companies_by_name

if __name__ == "__main__":
    asyncio.run(mcp.run())
