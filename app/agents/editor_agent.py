import asyncio

class EditorAgent:
    async def run(self, draft: str) -> str:
        await asyncio.sleep(0.1)
        # In a real system you’d fix grammar, tone, etc.
        improved = "Edited for clarity:\n\n" + draft
        return improved
