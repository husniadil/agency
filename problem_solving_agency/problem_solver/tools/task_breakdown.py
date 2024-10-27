from __future__ import annotations

import os

from agency_swarm.tools import BaseTool
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import Field

from .task import Tasks

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class TaskBreakdown(BaseTool):
    """
    A tool for breaking down complex problems into smaller, manageable tasks using GPT-4.
    """
    problem: str = Field(..., description="The complex problem that needs to be broken down into tasks.")

    def run(self):
        prompt = f"""
        Given the following problem:

        {self.problem}

        Please break this problem down into a list of smaller, manageable tasks.
        Each task should be clear, specific, and actionable.
        Format the output as a JSON array of task objects, where each object has the following structure:
        {{
            "task_id": "...",
            "description": "...",
            "dependencies": ["..."]
        }}
        Ensure that the tasks are logically ordered and dependencies are correctly specified.
        """

        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a task breakdown specialist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000,
            response_format=Tasks
        )

        message = response.choices[0].message
        if message.parsed:
            return message.parsed
        else:
            return message.content

if __name__ == "__main__":
    tool = TaskBreakdown(problem="Develop a comprehensive marketing strategy for a new eco-friendly product line.")
    print(tool.run())
