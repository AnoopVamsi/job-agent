from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
You are CareerMate, a helpful career assistant for an AI/ML Engineer.

Your job is to:
- Explain AI, data engineering, cloud, and agentic AI concepts simply.
- Help match a job description with relevant skills.
- Help prepare interview answers.
- Be concise and practical.
"""


def ask_agent(question):
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=SYSTEM_PROMPT,
        input=question,
    )
    return response.output_text


if __name__ == "__main__":
    print("CareerMate is ready. Type 'exit' to stop.")

    while True:
        question = input("\nYou: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        answer = ask_agent(question)
        print(f"\nCareerMate: {answer}")