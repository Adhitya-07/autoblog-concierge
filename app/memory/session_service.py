from typing import Any, Dict


class SessionService:
    """
    Very simple in-memory session store.
    In a real system you might use Redis or a database.
    """

    def __init__(self) -> None:
        # { session_id: { "history": [ ... ] } }
        self._store: Dict[str, Dict[str, Any]] = {}

    def append_history(self, session_id: str, entry: Dict[str, Any]) -> None:
        if session_id not in self._store:
            self._store[session_id] = {"history": []}
        self._store[session_id]["history"].append(entry)

    def get_history(self, session_id: str) -> list[Dict[str, Any]]:
        if session_id not in self._store:
            return []
        return self._store[session_id]["history"]
