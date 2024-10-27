from __future__ import annotations

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
    agency.run_demo()  # starts the agency in terminal
