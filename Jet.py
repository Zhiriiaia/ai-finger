import google.generativeai as genai
import time
import os
from datetime import datetime
from datetime import datetime
import pytz

# Configure Gemini API
genai.configure(api_key="AIzaSyDm5Pt3c8b1jWOlKkfU972npqHOaUZIWx4")

# Chat memory file path
chat_file = "txt files/chat_memory.txt"
os.makedirs("txt files", exist_ok=True)

# Count existing sessions
session_number = 1
if os.path.exists(chat_file):
    with open(chat_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.lower().startswith("session"):
                session_number += 1
else:
    with open(chat_file, "w") as f:
        f.write("")

# Read full past memory
with open(chat_file, "r") as f:
    past_convo = f.read()

# Load model with memory
model = genai.GenerativeModel("gemini-1.5-pro")
chat_session = model.start_chat(history=[{"role": "user", "parts": past_convo}])

# Write session header with number and time
session_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(chat_file, "a") as f:
    f.write(f"\n\nSession {session_number} ({session_time})\n")

def log_to_file(role, message):
    with open(chat_file, "a") as f:
        f.write(f"{role}: {message.strip()}\n")

def chat():
    print(f"Jet: Hey! This is Session {session_number}. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Jet: Goodbye!")
            break

        log_to_file("Me", user_input)

        # Check for time-related question
        time_keywords = ["what time", "current time", "tell me the time", "time is it"]
        if any(keyword in user_input.lower() for keyword in time_keywords):
            ph_timezone = pytz.timezone("Asia/Manila")
            current_time = datetime.now(ph_timezone).strftime("%I:%M %p")
            print("Jet:", f"The current time is {current_time}")
            log_to_file("Ai", f"The current time is {current_time}")
            continue

        try:
            response = chat_session.send_message(user_input)
            time.sleep(3)
            print("Jet:", response.text)
            log_to_file("Ai", response.text)
        except Exception as e:
            print("Jet: Oops, something went wrong!", e)

chat()
