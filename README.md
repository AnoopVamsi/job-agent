# CareerMate AI Agent

A beginner-friendly Python AI agent that acts as a career assistant for AI/ML Engineers.

It can help explain AI and cloud concepts, review job descriptions, and prepare interview answers.

## Features

- Conversational AI assistant
- AI/ML and data-engineering concept explanations
- Job-description skill matching
- Interview-preparation support
- Uses an OpenAI language model through the OpenAI API
- Keeps API keys private using a `.env` file

## Technology Stack

- Python 3.10+
- OpenAI Python SDK
- python-dotenv
- Git and GitHub

## Project Structure

```text
job-agent/
├── agent.py        # Main AI-agent application
├── .env            # Local API key file — never upload this
├── .gitignore      # Prevents secrets and local files from being committed
└── README.md        # Project documentation
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/AnoopVamsi/job-agent.git
cd job-agent
```

2. Install dependencies:

```bash
python3 -m pip install --user openai python-dotenv
```

3. Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

4. Run the agent:

```bash
python3 agent.py
```

## Example Questions

```text
What is RAG in simple terms?
Explain AWS Bedrock.
Help me prepare for an AI/ML Engineer interview.
How does an AI agent use tools?
```

## Security

Never upload your `.env` file or API key to GitHub. This project’s `.gitignore` excludes `.env` and `.venv/`.

## Next Steps

- Add tool calling for job-search APIs
- Add RAG over resumes and job descriptions
- Add a vector database
- Build a Streamlit web interface
- Deploy the agent to AWS or Azure

## Web User Interface

CareerMate includes a browser-based chat interface built with Streamlit.

Run the web application locally:

```bash
python3 -m streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

The interface lets users ask career, AI/ML, cloud, RAG, and interview-preparation questions through a simple chat screen.

## How It Works

```text
User → Streamlit web UI → CareerMate agent → OpenAI model → Answer
```