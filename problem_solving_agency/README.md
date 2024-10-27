# Problem Solving Agency

Welcome to the Problem Solving Agency repository! This project showcases a sophisticated AI-driven system designed to tackle complex problems by leveraging the power of the [Agency Swarm](https://github.com/VRSEN/agency-swarm) framework.

## Project Overview

The Problem Solving Agency is an advanced AI system that breaks down complex problems into manageable tasks, generates specialized AI agent profiles for each task, and executes these tasks using tailored AI agents. This approach allows for efficient and comprehensive problem-solving across various domains.

## Key Features

-   **Task Breakdown**: Utilizes GPT-4o-mini to analyze and decompose complex problems into structured, actionable tasks.
-   **Agent Profile Generation**: Creates specialized AI agent profiles tailored to the requirements of each specific task.
-   **Task Execution**: Executes tasks using generated agent profiles, ensuring optimal expertise for each component of the problem.
-   **Flexible Problem Solving**: Adaptable to a wide range of problem domains, from technical and scientific challenges to creative and strategic issues.

## Getting Started

### Prerequisites

-   Python 3.12 or higher
-   Docker (recommended for containerized deployment)

### Local Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/husniadil/agency.git
    cd agency
    cd problem_solving_agency
    ```

2. **Install Requirements**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:

    Create a `.env` file and add your [OpenAI API key](https://platform.openai.com/api-keys):

    ```
    OPENAI_API_KEY='your_openai_api_key_here'
    ```

4. **Run the Agency**:

    ```bash
    python agency.py
    ```

### Docker Installation (Recommended)

From the root of the project, run:

    ```bash
    docker compose up
    ```

### Check Your Assistant

Once you run the agency, you can check your assistant at [OpenAI Assistants](https://platform.openai.com/assistants).
