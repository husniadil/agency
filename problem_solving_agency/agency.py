from __future__ import annotations

import os

from agency_swarm import Agency
from problem_solver.problem_solver import ProblemSolver

problem_solver = ProblemSolver()

agency = Agency(
    [
        problem_solver,  # ProblemSolver will be the entry point for communication with the user
    ],
    shared_instructions='agency_manifesto.md',
    temperature=0.7,
    max_prompt_tokens=4000
)

if __name__ == "__main__":
    if os.getenv("RUN_GRADIO"):
        agency.demo_gradio(server_name="0.0.0.0", server_port=7860)  # starts the agency in gradio
    else:
        agency.run_demo()  # starts the agency in terminal
