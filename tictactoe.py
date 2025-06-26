import math
import random

# Tic-Tac-Toe board
board = [" "] * 9

def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("-" * 9)

def check_winner(player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in pattern) for pattern in win_patterns)

def is_full():
    return all(spot != " " for spot in board)

def minimax(depth, is_maximizing):
    if check_winner("X"): return -10 + depth
    if check_winner("O"): return 10 - depth
    if is_full(): return 0

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

def best_move():
    if random.random() < 0.3:  # 20% chance to make a bad move
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

def play_game():
    print("Tic-Tac-Toe (You: X, AI: O)")
    print_board()

    first_player = ""
    while first_player not in ["X", "O"]:
        first_player = input("Do you want to go first? (Y/N): ").strip().upper()
        if first_player == "Y":
            first_player = "X"
        elif first_player == "N":
            first_player = "O"
        else:
            print("Invalid choice! Please enter Y or N.")

    current_player = first_player

    while True:
        if current_player == "X":
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
        else:
            best_move()
            print("\nAI moves:")

        print_board()

        if check_winner(current_player):
            print(f"🎉 {current_player} wins!")
            break
        if is_full():
            print("😐 It's a draw!")
            break

        current_player = "X" if current_player == "O" else "O"

play_game()