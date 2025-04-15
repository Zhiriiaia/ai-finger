import time
import os

# Folder path where you want to store solves.txt
FOLDER_PATH = 'txt files'  # Change this to your desired folder name
SOLVES_FILE = os.path.join(FOLDER_PATH, 'solves.txt')

# Ensure the folder exists
if not os.path.exists(FOLDER_PATH):
    os.makedirs(FOLDER_PATH)  # Create the folder if it doesn't exist

# Load past solves from the file
def load_solves():
    if os.path.exists(SOLVES_FILE):
        with open(SOLVES_FILE, 'r') as file:
            return [float(line.strip()) for line in file.readlines()]
    return []  # Return an empty list if the file doesn't exist

# Save past solves to the file
def save_solves(past_solves):
    with open(SOLVES_FILE, 'w') as file:
        for solve in past_solves:
            file.write(f"{solve}\n")

# List to store past solve times
past_solves = load_solves()

# Function to print top 5 times
def print_top_times():
    if not past_solves:
        print("No solves recorded yet.")
        return
    print("Top 5 Best Times (in seconds):")
    top_times = sorted(past_solves)[:5]  # Get the best 5 solve times
    for i, solve in enumerate(top_times, 1):
        print(f"{i}. {solve:.2f}s")

# Function to start and stop the timer
def run_timer():
    print("Press 'start' to begin a solve or 'times' to see the top 5 best times.")
    
    running = False
    start_time = 0

    while True:
        user_input = input("Enter command: ").lower()  # Get input from the user

        if user_input == 's':  # Start the timer
            if not running:
                print("Get ready!")
                time.sleep(2)
                print("GO!!!")
                start_time = time.time()
                print("Timer started!")
                running = True
            else:
                elapsed_time = time.time() - start_time
                past_solves.append(elapsed_time)
                print(f"Timer stopped! Solve time: {elapsed_time:.2f} seconds")
                running = False
                save_solves(past_solves)  # Save solves after stopping the timer

        elif user_input == 'times':  # Show top 5 best times
            print_top_times()

        elif user_input == 'exit':  # Exit the program
            print("Exiting...")
            save_solves(past_solves)  # Save solves before exiting
            break

if __name__ == "__main__":
    run_timer()
