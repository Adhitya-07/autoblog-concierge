import asyncio
from .research_agent import ResearchAgent
from .writer_agent import WriterAgent
from .editor_agent import EditorAgent
from .seo_agent import SeoAgent
from ..memory.session_service import SessionService
from ..config import logger


class Orchestrator:
    def __init__(self) -> None:
        self.research_agent = ResearchAgent()
        self.writer_agent = WriterAgent()
        self.editor_agent = EditorAgent()
        self.seo_agent = SeoAgent()
        self.sessions = SessionService()

    async def run_pipeline(
        self,
        topic: str,
        audience: str | None = "general",
        session_id: str | None = None,
    ):
        # default session id if not provided
        if session_id is None:
            session_id = "default"

        logger.info(
            f"Starting pipeline | topic='{topic}', audience='{audience}', session_id='{session_id}'"
        )

        # 1) Research
        research_summary = await self.research_agent.run(topic)
        logger.info("Research step completed")

        # 2) Draft writing
        draft = await self.writer_agent.run(research_summary, audience or "general")
        logger.info("Writer step completed")

        # 3) Editing
        edited = await self.editor_agent.run(draft)
        logger.info("Editor step completed")

        # 4) SEO optimization
        seo_text = await self.seo_agent.run(edited, topic)
        logger.info("SEO step completed")

        # 5) Package final blog
        final_blog = await self.package(topic, seo_text, audience or "general")
        logger.info("Packaging step completed")

        # 6) Save to session history
        self.sessions.append_history(
            session_id,
            {
                "topic": topic,
                "audience": audience,
                "result": final_blog,
            },
        )
        logger.info(f"Saved result to session history for session_id='{session_id}'")

        return final_blog

    async def package(self, topic: str, content: str, audience: str) -> dict:
        await asyncio.sleep(0.05)
        title = f"Auto-generated blog on {topic} for {audience}"
        return {
            "title": title,
            "content": content,
        }
