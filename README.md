# MultiAgent Coder

MultiAgent Coder is an AI-powered development assistant that can help you build projects by converting natural language requests into structured, working code. The assistant uses multiple agents to break down your requests and implement each part of the project.

---

## Architecture

* **Planner Agent**: Analyzes your request and generates a detailed project plan.
* **Architect Agent**: Breaks down the plan into specific engineering tasks and provides context for each file.
* **Coder Agent**: Implements each task, writes the code into respective files, and uses tools to support development.

---

## Getting Started

### Prerequisites

1. Install `uv` by following the instructions [here](https://docs.astral.sh/uv/getting-started/installation/).
2. Create a Groq account and get your API key [here](https://console.groq.com/keys).

### Installation and Startup

1. Create a virtual environment:

   ```bash
   uv venv
   ```

2. Activate the virtual environment:

   ```bash
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   uv pip install -r pyproject.toml
   ```

4. Create a `.env` file and add the necessary variables and their values as specified in the `.sample_env` file.

5. Run the application:

   ```bash
   python main.py
   ```

---

## Example Prompts

* Create a to-do list application using HTML, CSS, and JavaScript.
* Create a simple calculator web application.
* Create a simple blog API using FastAPI with an SQLite database.