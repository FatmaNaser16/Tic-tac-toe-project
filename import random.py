import random
import tkinter as tk

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to evaluate the score of the board
def evaluate(board):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    else:
        return 0

# Function to check if the board is full
def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


def make_ai_move(board):
    best_eval = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                eval = minimax(board, 0, float('-inf'), float('inf'), False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = 'X'

# Function to make a move for the player
def make_player_move(row, col, board, buttons):
    if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
        board[row][col] = 'O'
        buttons[row][col].config(text='O', state='disabled')
        return True
    else:
        return False

# Main game loop
def play_game():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    buttons = [[0 for j in range(3)] for i in range(3)]

    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text=' ', font=('Arial', 20), width=5, height=2,
                                      command=lambda row=i, col=j: on_button_click(row, col))
            buttons[i][j].grid(row=i, column=j)

    def on_button_click(row, col):
        if make_player_move(row, col, board, buttons):
            if check_winner(board, 'O'):
                print("You win!")
                disable_all_buttons(buttons)
            elif is_board_full(board):
                print("It's a tie!")
                disable_all_buttons(buttons)
            else:
                print("AI's turn...")
                make_ai_move(board)
                print_board(board)
                if check_winner(board, 'X'):
                    print("AI wins!")
                    disable_all_buttons(buttons)
                elif is_board_full(board):
                    print("It's a tie!")
                    disable_all_buttons(buttons)

                # Update the buttons on the GUI
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 'X':
                            buttons[i][j].config(text='X', state='disabled')

    def disable_all_buttons(buttons):
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(state='disabled')

    print("Welcome to Tic-Tac-Toe!")
    root.mainloop()

# Start the game
play_game()