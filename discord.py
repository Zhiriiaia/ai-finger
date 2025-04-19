import requests
from datetime import datetime  # ✅ For getting the time

# Replace this with your Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1362350437088624772/oeOfpVBaUqFAvSmrKFQLsju3HxgMt3iqr9po1hxyDolp6LsDhWacHt40YpL-iKC2eZPr"

def send_message(username, message):
    payload = {
        "content": message,
        "username": username,
        "allowed_mentions": {"parse": []}  # Prevents mentions from pinging users
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(WEBHOOK_URL, json=payload, headers=headers)

    if response.status_code == 204:
        print(f"Message sent as {username}.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    while True:
        try:
            # Input format: {name}: {text}
            user_input = input("Enter message in format '{name}: {text}': ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            # Parse input
            if ":" not in user_input:
                print("Invalid format. Use '{name}: {text}'.")
                continue

            name_and_message = user_input.split(":", 1)
            username = name_and_message[0].strip()
            message = name_and_message[1].strip()

            # ✅ Check if message asks for time
            if "what time" in message.lower() or "current time" in message.lower() or "time now" in message.lower():
                current_time = datetime.now().strftime("%I:%M %p")
                send_message("Jet", f"The current time is {current_time}.")
                continue  # Skip sending original message

            # Send the message normally
            send_message(username, message)
        except Exception as e:
            print(f"An error occurred: {e}")
