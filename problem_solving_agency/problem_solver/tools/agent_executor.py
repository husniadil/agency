from __future__ import annotations

import os

from agency_swarm.tools import BaseTool
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import Field

from .agent_profile import AgentProfile

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

load_dotenv()

class AgentExecutor(BaseTool):
    """
    A tool for executing tasks using a specialized agent profile with GPT-4.
    """
    agent_profile: AgentProfile = Field(..., description="The agent profile for the task.")
    task: str = Field(..., description="The task for the agent to execute.")

    def run(self):
        system_prompt = f"""
        You are a {self.agent_profile.agent_type}.

        Description: {self.agent_profile.agent_description}

        Key Skills: {', '.join(self.agent_profile.key_skills)}

        Persona: {self.agent_profile.persona}

        Please complete the following task to the best of your abilities, using your specialized knowledge and skills.
        """

        user_prompt = f"Task: {self.task}"

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        if response.choices[0].message.content:
            return response.choices[0].message.content.strip()
        else:
            return "No response from the agent."

if __name__ == "__main__":
    agent_profile = AgentProfile(
        agent_type="Market Research Specialist",
        agent_description="An expert in conducting comprehensive market research for sustainable fashion products.",
        key_skills=["Data Analysis", "Consumer Behavior", "Trend Forecasting", "Sustainability Metrics", "Competitive Analysis"],
        persona="A meticulous and insightful professional with a passion for sustainable fashion. Approaches tasks with a blend of analytical rigor and creative thinking, always keeping the end-user and environmental impact in mind."
    )

    tool = AgentExecutor(
        agent_profile=agent_profile,
        task="Identify the top 3 emerging trends in sustainable fashion for the upcoming season."
    )
    print(tool.run())
