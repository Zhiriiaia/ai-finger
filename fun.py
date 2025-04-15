import time

while True:
    user_input = input("Type 'penis {number}' or 'exit' to quit: ")

    if user_input.lower() == "exit":
        print("Exiting...")
        time.sleep(0.5)
        break

    parts = user_input.split()
    if len(parts) == 2 and parts[0].lower() == "penis":
        try:
            num = int(parts[1])
            print("8" + "=" * num + "D")
        except ValueError:
            print("Invalid number. Try again!")

    else:
        print("Invalid format. Use: penis {number}")

    if user_input.lower() == "big":
        print("DAMN U BIG BOI")
        