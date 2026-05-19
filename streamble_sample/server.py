from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name="Simple_Streamble_MCP_example",
              host="localhost",
              port=8001,
              json_response=True)

@mcp.tool(name="Simple Addition Program")
def add(a:int , b:int)->int:

    return a+b

def main():
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
