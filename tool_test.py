from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

result = search_tool.run(
    "Tesla latest business strategy"
)

print(result)