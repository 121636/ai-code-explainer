import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_code(code: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional software engineer who explains code clearly and concisely."
                },
                {
                    "role": "user",
                    "content": f"Explain the following code in a structured way, including its purpose, logic, and key details:\n\n{code}"
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    print("=== AI Code Explainer ===")
    user_input = input("Enter code:\n")

    result = explain_code(user_input)

    print("\n=== Result ===\n")
    print(result)
