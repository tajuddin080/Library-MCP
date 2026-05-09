from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name = "hello World")

@mcp.tool(name = "greet",description="Say hello to someone")
def greet(name :str)->str:
    return f"Hello,{name}"


@mcp.tool(name = "scold",description="Curse Someone") #creating the mcp based tool
def scold(name:str)->str:
    return f"Hello ,{name}! you are cursed"


@mcp.tool(name = "addition",description="Perform addition based on the given numbers")
def add(a :int,b:int)->str:
    return f"The addition value of {a},{b} is {a+b}"


def main():
    #initialize and run the server
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()