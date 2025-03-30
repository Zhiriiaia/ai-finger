import google.generativeai as genai
import time

genai.configure(api_key="AIzaSyC_qFjmTI6nN_L5ezktCn04bRP8A0HJomY")

def chat():
    print("GeminiBot: Hey! Let's chat. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("GeminiBot: Goodbye!")
            break
        
        try:
            time.sleep(5)  # Delay before sending request
            response = genai.GenerativeModel("gemini-1.5-pro").generate_content(user_input)
            time.sleep(5)  # Delay before showing response
            print("GeminiBot:", response.text)
        except Exception as e:
            print("GeminiBot: Oops, something went wrong!", e)

chat()
