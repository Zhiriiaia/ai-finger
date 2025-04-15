import os
import time


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