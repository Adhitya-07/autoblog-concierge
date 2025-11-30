import asyncio

class SeoAgent:
    async def run(self, edited_text: str, topic: str) -> str:
        await asyncio.sleep(0.1)
        # Simulate adding SEO hints
        seo_note = (
            f"[SEO NOTE] Make sure to include the phrase '{topic}' "
            f"in headings and meta description.\n\n"
        )
        return seo_note + edited_text
