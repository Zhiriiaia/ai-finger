import math
import random

# Tic-Tac-Toe board
board = [" "] * 9

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("-" * 9)

# Function to check for a winner
def check_winner(player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in pattern) for pattern in win_patterns)

# Function to check if the board is full (draw)
def is_full():
    return all(spot != " " for spot in board)

# Minimax algorithm for AI
def minimax(depth, is_maximizing):
    if check_winner("X"): return -10 + depth  # Human wins
    if check_winner("O"): return 10 - depth   # AI wins
    if is_full(): return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move function (sometimes makes bad moves)
def best_move():
    if random.random() < 0.2:  # 20% chance AI makes a bad move
        available_moves = [i for i in range(9) if board[i] == " "]
        board[random.choice(available_moves)] = "O"
        return
    
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Main game loop
def play_game():
    print("Tic-Tac-Toe (You: X, AI: O)")
    print_board()
    
    # Choose who goes first
    while True:
        first = input("Do you want to go first? (y/n): ").strip().lower()
        if first in ["y", "n"]:
            break
        print("Invalid input! Please enter 'y' or 'n'.")
    
    human_turn = first == "y"
    
    while True:
        if human_turn:
            # Human move
            while True:
                try:
                    user_move = int(input("\nEnter your move (1-9): ")) - 1
                    if board[user_move] == " ":
                        board[user_move] = "X"
                        break
                    else:
                        print("Spot taken, choose another!")
                except (ValueError, IndexError):
                    print("Invalid move! Choose 1-9.")

            print_board()

            if check_winner("X"):
                print("🎉 You win!")
                break
            if is_full():
                print("😐 It's a draw!")
                break
        else:
            # AI move
            best_move()
            print("\nAI moves:")
            print_board()

            if check_winner("O"):
                print("🤖 AI wins!")
                break
            if is_full():
                print("😐 It's a draw!")
                break
        
        human_turn = not human_turn

# Run the game
play_game()
