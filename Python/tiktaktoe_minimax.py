import tkinter as tk
import random

# Initialize global variables for the board and player
player = "X"
ai = "O"
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to check if a player has won
def check_win(b, sign):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([b[i][j] == sign for j in range(3)]) or all([b[j][i] == sign for j in range(3)]):
            return True
    if b[0][0] == sign and b[1][1] == sign and b[2][2] == sign:
        return True
    if b[0][2] == sign and b[1][1] == sign and b[2][0] == sign:
        return True
    return False

# Function to check if the game is a draw
def check_draw(b):
    return all([b[i][j] != " " for i in range(3) for j in range(3)])

# Minimax algorithm to evaluate the best move for the AI
def minimax(b, depth, is_maximizing):
    if check_win(b, ai):  # AI wins
        return 10 - depth
    elif check_win(b, player):  # Player wins
        return depth - 10
    elif check_draw(b):  # Draw
        return 0

    if is_maximizing:
        best = -float("inf")
        for i in range(3):
            for j in range(3):
                if b[i][j] == " ":
                    b[i][j] = ai
                    best = max(best, minimax(b, depth + 1, False))
                    b[i][j] = " "
        return best
    else:
        best = float("inf")
        for i in range(3):
            for j in range(3):
                if b[i][j] == " ":
                    b[i][j] = player
                    best = min(best, minimax(b, depth + 1, True))
                    b[i][j] = " "
        return best

# Function to get the best move for the AI
def best_move():
    best_val = -float("inf")
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val

    return move

# Function to handle a player's move
def player_move(i, j):
    if board[i][j] == " ":
        board[i][j] = player
        buttons[i][j].config(text=player)  # Update the button text
        if check_win(board, player):
            display_winner("Player")
        elif check_draw(board):
            display_winner("Draw")
        else:
            ai_move()

# Function for the AI's move
def ai_move():
    i, j = best_move()
    board[i][j] = ai
    buttons[i][j].config(text=ai)  # Update the button text
    if check_win(board, ai):
        display_winner("AI")
    elif check_draw(board):
        display_winner("Draw")

# Function to display the winner
def display_winner(winner):
    if winner == "Player":
        result_label.config(text="Player Wins!")
    elif winner == "AI":
        result_label.config(text="AI Wins!")
    else:
        result_label.config(text="It's a Draw!")
    for button in buttons:
        for btn in button:
            btn.config(state="disabled")  # Disable all buttons after the game ends

# Function to reset the game
def reset_game():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]  # Reset the board
    result_label.config(text="")  # Clear the result label
    # Re-enable buttons and clear their text
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state="normal")

# Set up the GUI with Tkinter
root = tk.Tk()
root.title("AI-based Tic-Tac-Toe")

# Create buttons for the game board
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, font=('normal', 20), 
                                  command=lambda i=i, j=j: player_move(i, j))
        buttons[i][j].grid(row=i, column=j)

# Result display label
result_label = tk.Label(root, text="", font=('normal', 20))
result_label.grid(row=3, column=0, columnspan=3)

# Reset button
reset_button = tk.Button(root, text="Reset Game", font=('normal', 14), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

# Run the application
root.mainloop()