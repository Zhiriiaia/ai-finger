import google.generativeai as genai
import time, os, requests
from datetime import datetime
import pytz
from PIL import Image
from io import BytesIO

# Configure Gemini API
genai.configure(api_key="AIzaSyDm5Pt3c8b1jWOlKkfU972npqHOaUZIWx4")

# Chat memory file path
chat_file = "txt files/chat_memory.txt"
os.makedirs("txt files", exist_ok=True)
os.makedirs("images", exist_ok=True)

# Count sessions
session_number = 1 
if os.path.exists(chat_file):
    with open(chat_file, "r") as f:
        session_number += sum(1 for line in f if line.lower().startswith("session"))
else:
    open(chat_file, "w").close()

# Load memory
with open(chat_file, "r") as f:
    past_convo = f.read()

# Start chat
model = genai.GenerativeModel("gemini-1.5-pro")
chat_session = model.start_chat(history=[{"role": "user", "parts": past_convo}])

# Write session header
session_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(chat_file, "a") as f:
    f.write(f"\n\nSession {session_number} ({session_time})\n")

def log_to_file(role, message):
    with open(chat_file, "a") as f:
        f.write(f"{role}: {message.strip()}\n")

def generate_image(prompt):
    try:
        url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        img_path = f"images/generated_{timestamp}.png"
        img.save(img_path)
        return f"Image saved as {img_path}"
    except Exception as e:
        return f"Image generation failed: {e}"

def chat():
    print(f"Jet: Hey! This is Session {session_number}. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Jet: Goodbye!")
            break

        log_to_file("Me", user_input)

        # Time check
        time_keywords = ["what time", "current time", "tell me the time", "time is it"]
        if any(keyword in user_input.lower() for keyword in time_keywords):
            ph_time = datetime.now(pytz.timezone("Asia/Manila")).strftime("%I:%M %p")
            print("Jet:", f"The current time is {ph_time}")
            log_to_file("Ai", f"The current time is {ph_time}")
            continue

        # Image generation check
        if "generate an image" in user_input.lower():
            prompt = user_input.lower().replace("generate an image", "").strip()
            if not prompt:
                prompt = "fantasy castle landscape"
            result = generate_image(prompt)
            print("Jet:", result)
            log_to_file("Ai", result)
            continue

        exit_keywords = ["bye", "see you", "shutdown"]
        response = chat_session.send_message(user_input)
        if any(keyword in user_input.lower() for keyword in exit_keywords):
            print("Jet:", response.text)
            break

        try:
            response = chat_session.send_message(user_input)
            with open(chat_file, "r") as f: #possibly not working, this is so it checks the memory live while chatting
                past_convo = f.read()
            time.sleep(2)
            print("Jet:", response.text)
            log_to_file("Ai", response.text)
        except Exception as e:
            print("Jet: Oops, something went wrong!", e)

chat()