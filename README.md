# AutoBlog Concierge – Multi-Agent Blog Writer

## 1. Project Overview

This project is built for the **Concierge Agents** track of the Kaggle AI Agents capstone.

**Problem:**  
Writing blog posts is slow and mentally tiring. Research, drafting, editing, and SEO all take time and focus.

**Solution:**  
AutoBlog Concierge is a **multi-agent system** that:
- researches a topic on the web,
- drafts a blog for a specific audience,
- edits it for clarity,
- adds simple SEO hints,
- and stores results per user session.

You call one API: `/generate`.  
It returns a ready-to-use blog post.

---

## 2. Features & Concepts Demonstrated

This project covers multiple required concepts:

### ✅ Multi-agent system
Agents:
- `ResearchAgent` – calls a web search tool and builds a research summary  
- `WriterAgent` – drafts the blog using the research summary  
- `EditorAgent` – cleans up and improves the draft  
- `SeoAgent` – adds SEO hints (keywords in titles, meta description guidance)  
- `Orchestrator` – coordinates all agents in sequence and handles sessions

### ✅ Tools
- `WebSearchTool` (`app/tools/search_tool.py`)  
  - Uses **httpx** to call DuckDuckGo search (`GET https://duckduckgo.com/html`)  
  - Parses basic HTML chunks into text snippets used by the research agent

### ✅ Sessions & Memory
- `SessionService` (`app/memory/session_service.py`)  
  - Stores history per `session_id` in memory  
  - Accessible via `/history/{session_id}` endpoint  

### ✅ Observability
- Central `logger` in `app/config.py`  
- Orchestrator logs:
  - pipeline start  
  - each agent completion step  
  - saving to session history  

---

## 3. Architecture

**High-level flow:**

1. Client calls `POST /generate` with:
   - `topic`
   - `audience`
   - optional `session_id`
2. `Orchestrator.run_pipeline()` runs agents in order:
   - `ResearchAgent.run(topic)`
   - `WriterAgent.run(research, audience)`
   - `EditorAgent.run(draft)`
   - `SeoAgent.run(edited, topic)`
   - `package()` final blog
3. Result stored in `SessionService` under `session_id`
4. Client can fetch history via `GET /history/{session_id}`

**Folder structure (key parts only):**

```text
autoblog-concierge/
  app/
    main.py                 # FastAPI app & endpoints
    config.py               # logging config
    agents/
      orchestrator.py
      research_agent.py
      writer_agent.py
      editor_agent.py
      seo_agent.py
      publisher_agent.py    # (placeholder for future publish step)
    tools/
      search_tool.py        # web search tool (httpx + DuckDuckGo)
    memory/
      session_service.py    # in-memory session store
  requirements.txt
  README.md
