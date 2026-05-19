from mcp.server.fastmcp import FastMCP

mcp = FastMCP("library-MCP")


@mcp.tool("Add Book",description="Used to add book to the library")
async def add_book(book_name:str):
    return f"The book {book_name} is added to Library"



def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
