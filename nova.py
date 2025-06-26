from openai import OpenAI
import os
from datetime import datetime

# Setup Kluster.ai client
client = OpenAI(
    api_key="0ccb5c30-71bd-4b71-8c70-a56b0c1d54b5",
    base_url="https://api.kluster.ai/v1",
)

# Create memory folder if not exists
os.makedirs("files", exist_ok=True)
memory_file = "txt files/Nova.txt"

# Load past memory
def load_memory():
    if not os.path.exists(memory_file):
        return []
    with open(memory_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    messages = []
    for line in lines:
        if line.startswith("User: "):
            messages.append({"role": "user", "content": line[6:].strip()})
        elif line.startswith("Nova: "):
            messages.append({"role": "assistant", "content": line[6:].strip()})
    return messages

# Save new memory
def save_message(role, content):
    with open(memory_file, "a", encoding="utf-8") as f:
        f.write(f"{role}: {content}\n")

# Start chat
def chat():
    print("Nova is ready! (Type 'exit' to quit)\n")
    history = load_memory()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Nova: Goodbye!")
            break

        # Add user message to history
        history.append({"role": "user", "content": user_input})

        # Request response from Kluster
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=history,
            temperature=7,
            max_completion_tokens=4000
        )

        bot_reply = response.choices[0].message.content.strip()
        print(f"Nova: {bot_reply}")

        # Save both user and bot messages
        save_message("User", user_input)
        save_message("Nova", bot_reply)

        # Update history
        history.append({"role": "assistant", "content": bot_reply})

if __name__ == "__main__":
    chat()
