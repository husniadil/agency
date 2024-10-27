from __future__ import annotations

from typing import List

from pydantic import BaseModel


class AgentProfile(BaseModel):
    """
    A specialized agent profile for a given task.
    """
    agent_type: str
    agent_description: str
    key_skills: list[str]
    persona: str
