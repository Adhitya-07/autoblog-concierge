import asyncio
from ..tools.search_tool import WebSearchTool


class ResearchAgent:
    def __init__(self) -> None:
        self.search_tool = WebSearchTool()

    async def run(self, topic: str) -> str:
        # Call the web search tool
        snippets = await self.search_tool.search(topic, max_results=2)

        await asyncio.sleep(0.05)  # small simulated processing delay

        # Build a readable research summary from raw snippets
        bullet_points = []
        for idx, snip in enumerate(snippets, start=1):
            # keep each snippet shorter so it’s not crazy long
            shortened = snip.replace("\n", " ")[:300]
            bullet_points.append(f"- Source {idx}: {shortened}...")

        summary = (
            f"Research summary for topic '{topic}':\n"
            f"This summary is built from {len(snippets)} web sources.\n\n"
            + "\n".join(bullet_points)
        )

        return summary
