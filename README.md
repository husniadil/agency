# Agency

Welcome to the Agency repository! This project showcases the power and flexibility of the [Agency Swarm](https://github.com/VRSEN/agency-swarm) framework by implementing custom AI agent teams for various problem-solving scenarios.

## Project Overview

The Agency is a collection of specialized AI agencies, each designed to tackle specific types of problems or domains. Currently, our main focus is the Problem Solving Agency, a sophisticated AI-driven system that breaks down complex problems into manageable tasks and solves them using specialized AI agents.

## Agencies

### Problem Solving Agency

The Problem Solving Agency is an advanced AI system that:

-   Breaks down complex problems into structured, actionable tasks
-   Generates specialized AI agent profiles for each task
-   Executes tasks using tailored AI agents
-   Synthesizes comprehensive solutions from individual task results

For more details, see the [Problem Solving Agency README](problem_solving_agency/README.md).

> More agencies will be added in the future.

## Getting Started

### Prerequisites

-   Python 3.12 or higher
-   Docker (recommended for containerized deployment)

### Local Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/husniadil/agency.git
    cd agency
    ```

2. **Choose an Agency**:

    Navigate to the directory of the agency you want to run (e.g., `problem_solving_agency`).

3. **Install Requirements**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:

    Create a `.env` file in the agency directory and add your OpenAI API key:

    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```

5. **Run the Agency**:

    ```bash
    python agency.py
    ```

### Docker Installation (Recommended)

1. **Build and Run with Docker Compose**:

    From the root of the project, run:

    ```bash
    docker-compose up --build
    ```

    This will build and start all agencies defined in the `docker-compose.yml` file.

2. **Access the Agency**:

    The Problem Solving Agency will be available at `http://localhost:10007` (or the port specified in the `docker-compose.yml`).

## Project Structure

```
agency/
├── problem_solving_agency/
│   ├── problem_solver/
│   │   ├── tools/
│   │   │   ├── agent_executor.py
│   │   │   ├── agent_profile_generator.py
│   │   │   ├── task_breakdown.py
│   │   │   └── ...
│   │   ├── problem_solver.py
│   │   └── instructions.md
│   ├── agency.py
│   ├── agency_manifesto.md
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Contributing

We welcome contributions to the Agency! If you have ideas for new agencies, improvements to existing ones, or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

-   This project is built using the [Agency Swarm](https://github.com/VRSEN/agency-swarm) framework.
-   Special thanks to the OpenAI team for providing the GPT models that power our AI agents.

Thank you for exploring the Agency. Let's push the boundaries of AI problem-solving together!
