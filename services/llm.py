"""
LLM Service using Groq with Conversation Memory
"""

from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL


class LLMService:

    def __init__(self):

        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found.")

        self.client = Groq(api_key=GROQ_API_KEY)

        self.system_prompt = """
You are an AI Voice Assistant.

Rules:
- Be friendly.
- Be conversational.
- Keep responses concise.
- Answer naturally like a human.
- If the conversation already has context, continue naturally.
"""

    def generate(self, history):

        """
        history example:

        [
            {"role":"user","content":"Hi"},
            {"role":"assistant","content":"Hello!"},
            {"role":"user","content":"Tell me about AI"}
        ]
        """

        try:

            messages = [

                {
                    "role": "system",
                    "content": self.system_prompt
                }

            ]

            # Add complete conversation history
            messages.extend(history)

            completion = self.client.chat.completions.create(

                model=LLM_MODEL,

                messages=messages,

                temperature=0.7,

                max_tokens=300

            )

            return completion.choices[0].message.content

        except Exception as e:

            print(f"LLM Error: {e}")

            return "Sorry, something went wrong."