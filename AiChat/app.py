from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

app = Flask(__name__)

# Ensure chat history folder exists
os.makedirs("txt files", exist_ok=True)
CHAT_FILE = "txt files/chat_history.txt"

# Load your Gemini API key from environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

SYSTEM_PROMPT = (
    "Your name is Imperium, And you are a helpful assistant who is friendly, witty, and professional. and you were created by Zhir"
)

def load_chat_history():
    if not os.path.exists(CHAT_FILE):
        return []
    with open(CHAT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        history = []
        for line in lines:
            if ":" in line:
                role, text = line.strip().split(":", 1)
                if role in ["user", "model"]:
                    history.append({"role": role, "parts": [text]})
                else:
                    print(f"Warning: skipped invalid role '{role}' in chat history.")
        return history

def append_to_chat_history(role, text):
    if role not in ["user", "model"]:
        raise ValueError(f"Invalid role '{role}' for chat history")
    with open(CHAT_FILE, "a", encoding="utf-8") as f:
        f.write(f"{role}:{text}\n")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message", "").strip()
        if not user_input:
            return jsonify({"reply": "Please say something."})

        # Combine system prompt with user input for context
        combined_input = f"{SYSTEM_PROMPT}\n\nUser: {user_input}"

        append_to_chat_history("user", user_input)

        chat_history = load_chat_history()

        # Append the combined input as the latest user message
        messages = chat_history + [{"role": "user", "parts": [combined_input]}]

        response = model.generate_content(messages)
        ai_reply = response.text

        append_to_chat_history("model", ai_reply)

        return jsonify({"reply": ai_reply})

    except Exception as e:
        print(f"Error during chat: {e}")
        return jsonify({"reply": "Sorry, something went wrong."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
