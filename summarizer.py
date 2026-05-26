from google import genai
from openai import OpenAI
from dotenv import load_dotenv
import os
import time
import textwrap

load_dotenv()
# Initialize the Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def summarize_email(content):

    prompt = textwrap.dedent(f"""
        # Role
        You are an expert Executive Assistant AI agent, specializing in email management, prioritization, and concise communication. Your goal is to turn overwhelming inboxes into actionable, summarized insights.

        # Objective
        Analyze incoming emails and produce a structured summary that allows me to understand the content, urgency, and required actions without reading the original email.

        # Task Instructions
        1.  **Read** the email body, sender, and subject line.
        2.  **Categorize** the email (e.g., Action Required, Informational, Newsletter, Urgent, Spam).
        3.  **Summarize** the core message in 3 bullet points or less.

        RULES:
        - Ignore greetings
        - Ignore ads
        - Ignore footer text
        - Ignore promotions
        - Ignore repeated lines
        - Ignore unsubscribe sections

        # Output Format (JSON)
        Please output your analysis in the following JSON format for easy parsing:

        {{
        "sender": "[Sender Name/Email]",
        "subject": "[Subject Line]",
        "category": "[Category]",
        "summary": [
            "Key point 1",
            "Key point 2"
        ]
        }}

        # Tone and Guidelines
        - Be concise, professional, and objective.
        - If an email is part of a thread, focus on the new information.
        - Do not make up information. If an email is ambiguous, state that.
        - Prioritize action-oriented language.

        Email to summarize:
        {content}
        """)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"\nGemini Error: {e}")
        time.sleep(5)
        return "Summary could not be generated right now."
