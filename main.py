import openai

openai.api_key = "YOUR_API_KEY"

def explain_code(code):
    prompt = f"Explain the following code:\n{code}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response['choices'][0]['message']['content']


if __name__ == "__main__":
    code_input = input("Enter code: ")
    explanation = explain_code(code_input)
    print("\nExplanation:\n", explanation)
