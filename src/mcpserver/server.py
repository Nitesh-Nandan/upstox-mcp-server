from mcp.server.fastmcp import FastMCP
from auth import save_token


mcp = FastMCP("Upstox-MCP-Server")


@mcp.tool()
def helloWorld() -> str:
    """
    Returns 'Hello from upstox-mcp-server!'
    """
    print("Hello from upstox-mcp-server!")
    return "Hello from upstox-mcp-server!"


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



    

if __name__ == "__main__":
    mcp.run()
