from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_chatgpt_response(prompt):
    msgs = [
            {
                "role": "user",
                "content": prompt
            }
        ]
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=msgs,
    )
    
    return completion.choices[0].message.content


# Usage example
if __name__ == "__main__":
     print("Welcome to chatGPT CLI. Type 'exit' to quit.")
     while True:
        user_input = input("Ask ChatGPT: ")
        if user_input.lower() == "exit":
            print("Goodbye")
            break

        chatgpt_response = generate_chatgpt_response(user_input)
        if chatgpt_response:
            print(f"ChatGPT says: {chatgpt_response}")