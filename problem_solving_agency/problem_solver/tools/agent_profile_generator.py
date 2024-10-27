from __future__ import annotations

import os

from agency_swarm.tools import BaseTool
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import Field

from .agent_profile import AgentProfile

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

load_dotenv()

class AgentProfileGenerator(BaseTool):
    """
    A tool for generating specialized agent profiles based on task requirements using GPT-4.
    """
    task: str = Field(..., description="The task for which a specialized agent profile needs to be generated.")

    def run(self):
        prompt = f"""
        Given the following task:

        {self.task}

        Please create a specialized agent profile to handle this task. Provide the following details:
        1. Agent Type: A short, descriptive name for the type of agent.
        2. Agent Description: A brief description of the agent's role and capabilities.
        3. Key Skills: List 3-5 key skills or areas of expertise this agent should possess.
        4. Persona: A short paragraph describing the agent's personality and approach to tasks.

        Return the agent profile in JSON format with the following structure:
        {{
            "agent_type": "...",
            "agent_description": "...",
            "key_skills": ["..."],
            "persona": "..."
        }}
        """

        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI agent profile creation specialist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500,
            response_format=AgentProfile
        )

        message = response.choices[0].message
        if message.parsed:
            return message.parsed
        else:
            return message.content

if __name__ == "__main__":
    tool = AgentProfileGenerator(task="Conduct market research for a new line of sustainable fashion products")
    print(tool.run())
