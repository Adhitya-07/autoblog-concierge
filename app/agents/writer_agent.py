import asyncio

class WriterAgent:
    async def run(self, research_summary: str, audience: str) -> str:
        await asyncio.sleep(0.1)
        draft = (
            f"Blog draft for {audience}:\n\n"
            f"Introduction:\n"
            f"{research_summary}\n\n"
            f"Main Content:\n"
            f"- Key idea 1 explained in simple terms.\n"
            f"- Key idea 2 with an example.\n"
            f"- Key idea 3 with an action step.\n\n"
            f"Conclusion:\n"
            f"This draft is generated automatically to help you move faster."
        )
        return draft
