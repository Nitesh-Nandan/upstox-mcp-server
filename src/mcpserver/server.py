from mcp.server.fastmcp import FastMCP
from auth import save_token
from models import Exchange
from utils import instrumentCache
from marketdata import get_last_traded_price

mcp = FastMCP("Upstox-MCP-Server")


@mcp.tool()
def refresh_access_token(token: str):
    """
    Get the access token from the user and save it to both environment variable and .env file
    Args:
        token (str): The access token to be saved. Leading/trailing whitespace will be automatically stripped.
    Returns:
        str: A success message confirming the token has been saved to both 
             the environment variable and .env file.
    """
    return save_token(token)

@mcp.tool()
def get_ltp(symbol: str, exchange: Exchange = Exchange.NSE_EQ):
    """
    Get the last traded price of a given symbol and exchange
    Args:
        symbol (str): The symbol of the instrument
        exchange (Exchange): The exchange of the instrument defaults to NSE_EQ
    """
    instruments = instrumentCache.get_instrument(symbol, exchange)

    return get_last_traded_price(instruments)


if __name__ == "__main__":
    mcp.run()
