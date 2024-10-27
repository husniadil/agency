from __future__ import annotations

from agency_swarm import Agent

from .tools.agent_executor import AgentExecutor
from .tools.agent_profile_generator import AgentProfileGenerator
from .tools.task_breakdown import TaskBreakdown


class ProblemSolver(Agent):
    def __init__(self):
        super().__init__(
            name="ProblemSolver",
            description="Analyzes problems, breaks them down into tasks, generates specialized agent profiles, and executes tasks using these profiles.",
            instructions="./instructions.md",
            tools=[TaskBreakdown, AgentProfileGenerator, AgentExecutor],
            temperature=0.7,
            max_prompt_tokens=4000,
            model="gpt-4o-mini"
        )
