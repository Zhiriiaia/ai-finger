import wikipediaapi
import requests
from PIL import Image
from io import BytesIO
import os

wiki = wikipediaapi.Wikipedia(language='en', user_agent='JetScienceBot/1.0')

os.makedirs("wiki", exist_ok=True)

def search_wikipedia(query):
    page = wiki.page(query)
    if page.exists():
        summary = page.summary
        return summary
    else:
        return "I couldn’t find anything on that."

def fetch_image(prompt):
    try:
        url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img_path = f"wiki/{prompt.replace(' ', '_')}.png"
        img.save(img_path)
        return f"Image saved as {img_path}"
    except Exception as e:
        return f"Image fetch failed: {e}"

def science_bot():
    print("JetWiki: Hey, ask me anything. Type 'shutdown' to quit.")

    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "shutdown":
            print("JetWiki: Shutting down...")
            break

        if user_input.startswith("show image of"):
            prompt = user_input.replace("show image of", "").strip()
            if prompt:
                result = fetch_image(prompt)
                print("JetWiki:", result)
            else:
                print("JetWiki: You need to say what image you want.")
        else:
            response = search_wikipedia(user_input)
            print("JetWiki:", response)

science_bot()
