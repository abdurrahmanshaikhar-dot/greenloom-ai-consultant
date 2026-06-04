from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from duckduckgo_search import DDGS


class SearchInput(BaseModel):
    query: str = Field(
        ...,
        description="Search query"
    )


class DuckDuckGoTool(BaseTool):
    name: str = "DuckDuckGo Search Tool"
    description: str = (
        "Searches DuckDuckGo for recent information."
    )

    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
        try:
            with DDGS() as ddgs:
                results = list(
                    ddgs.text(
                        query,
                        max_results=5
                    )
                )

            if not results:
                return "No results found."

            output = []

            for result in results:
                output.append(
                    f"""
Title: {result.get('title', '')}
URL: {result.get('href', '')}
Snippet: {result.get('body', '')}
"""
                )

            return "\n".join(output)

        except Exception as e:
            return f"Search Error: {str(e)}"