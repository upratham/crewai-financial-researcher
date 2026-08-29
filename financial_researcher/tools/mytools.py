"""Custom tools for the financial_researcher crew.

Referenced from an agent or task JSONC as ``custom:mytools``. When the crew
loads, CrewAI executes this file and instantiates the first
``crewai.tools.BaseTool`` subclass it finds here (no constructor arguments).

This wraps the built-in Serper (google.serper.dev) search so we can tune it
for company research. It still needs ``SERPER_API_KEY`` in the environment.
Get a free key at https://serper.dev.
"""

import crewai_tools


class WebSearchTool(crewai_tools.SerperDevTool):
    """Google web search tuned for company/financial research.

    Same interface as the stock ``SerperDevTool`` — call it with a
    ``search_query`` string — but returns more results per query so the
    researcher gets broader coverage in a single call.
    """

    name: str = "Web search"
    description: str = (
        "Search the web with a `search_query` string. Returns the top organic "
        "results (title, link, snippet), plus a knowledge-graph summary and "
        "related questions when available. Use it to find recent news, "
        "filings, financials, and background on a company."
    )

    # Override stock SerperDevTool defaults.
    n_results: int = 15
    search_type: str = "search"  # switch to "news" for recent-headlines mode
