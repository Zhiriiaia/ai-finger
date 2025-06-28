import google.generativeai as genai
import os

# Configure with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# System prompt: this is your "fine-tuned" behavior
system_instruction = (
    "be a human, like do, Hey! how are you, etc. "
    "do EVERYTHING your chatter says you to but act like a human, nice and cool."
)

# Create the model with generation config
model = genai.GenerativeModel(
    model_name="models/gemini-2.0-flash",
    system_instruction=system_instruction,
    generation_config=genai.types.GenerationConfig(
        temperature=0,
        max_output_tokens=1000,
    )
)

# Simple terminal loop
print("✅ Gemini 2.0 Flash Ready — Type a number to increment it. Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ["exit", "quit"]:
        break
    response = model.generate_content(user_input)
    print("Gemini:", response.text.strip())
