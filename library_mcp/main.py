from mcp.server.fastmcp import FastMCP

mcp = FastMCP("library-MCP")


@mcp.tool("")



def main():
    print("Hello from library-mcp!")


if __name__ == "__main__":
    main()
