import httpx
from typing import List


class WebSearchTool:
    """
    Very simple web search tool using an HTTP GET request.
    For the capstone, this counts as a custom tool that calls the web.

    It tries to fetch HTML from DuckDuckGo's search page and returns
    a few text snippets. If anything fails, it returns a fallback string.
    """

    async def search(self, query: str, max_results: int = 3) -> List[str]:
        url = "https://duckduckgo.com/html/"
        params = {"q": query}

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.get(url, params=params)
                resp.raise_for_status()
        except Exception as e:
            # Fallback if no internet / blocked / error
            return [
                f"(fallback) Could not reach search service. "
                f"Using a simple generic summary about '{query}'. Error: {e}"
            ]

        # Very rough parsing: just take chunks of the HTML text as "snippets"
        text = resp.text
        # cut the page into chunks and take first few as pseudo-snippets
        chunk_size = 400
        snippets: List[str] = []
        for i in range(0, min(len(text), chunk_size * max_results), chunk_size):
            snippets.append(text[i : i + chunk_size])

        if not snippets:
            snippets = [f"(fallback) No content parsed for query '{query}'"]

        return snippets[:max_results]
