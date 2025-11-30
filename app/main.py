from fastapi import FastAPI
from pydantic import BaseModel
from .agents.orchestrator import Orchestrator

app = FastAPI()
orch = Orchestrator()

class GenerateRequest(BaseModel):
    topic: str
    audience: str | None = "general"
    session_id: str | None = None


@app.post("/generate")
async def generate_post(body: GenerateRequest):
    result = await orch.run_pipeline(
        topic=body.topic,
        audience=body.audience,
        session_id=body.session_id,
    )
    return {"status": "ok", "data": result}


@app.get("/history/{session_id}")
async def get_history(session_id: str):
    history = orch.sessions.get_history(session_id)
    return {"session_id": session_id, "history": history}
