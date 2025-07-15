from mcp.server.fastmcp import FastMCP
from marketdata import sayHello

mcp = FastMCP("Upstox-MCP-Server")


@mcp.tool()
def helloWorld() -> str:
    """
    Returns 'Hello from upstox-mcp-server!'
    """
    print("Hello from upstox-mcp-server!")
    return "Hello from upstox-mcp-server!"


if __name__ == "__main__":
    mcp.run()
