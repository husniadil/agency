from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Tasks(BaseModel):
    """
    A list of tasks.
    """
    tasks: list[str]
