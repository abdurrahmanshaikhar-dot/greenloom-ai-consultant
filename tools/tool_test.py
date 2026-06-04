from tools.search_tool import DuckDuckGoTool

tool = DuckDuckGoTool()

print(
    tool.run(
        query="Tesla business strategy 2026"
    )
)