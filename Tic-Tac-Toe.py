import tkinter as tk
from tkinter import messagebox

# Initialize the game
game = [[None, None, None],
        [None, None, None],
        [None, None, None]]
player = 'X'

# Check if there is a winner
def check_winner():
    # Check rows
    for row in game:
        if row.count(row[0]) == len(row) and row[0] is not None:
            return True

    # Check columns
    for col in range(len(game)):
        if game[0][col] == game[1][col] == game[2][col] and game[0][col] is not None:
            return True

    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] is not None:
        return True
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] is not None:
        return True

    return False

# Update the game state and UI
def update_game_state(row, col, button):
    global player

    # Update the game state
    game[row][col] = player

    # Update the button text
    button.config(text=player)

    # Check if there is a winner
    if check_winner():
        messagebox.showinfo("Game Over", f"Player {player} wins!")
        reset_game()
        return

    # Switch to the next player
    player = 'O' if player == 'X' else 'X'

# Handle button click event
def handle_button_click(row, col):
    button = buttons[row][col]
    if game[row][col] is None:
        update_game_state(row, col, button)
    else:
        messagebox.showerror("Invalid Move", "That cell is already occupied.")

# Reset the game state and UI
def reset_game():
    global game, player
    game = [[None, None, None],
            [None, None, None],
            [None, None, None]]
    player = 'X'
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text='')

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create the buttons
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text='', width=10, height=5,
                           command=lambda r=row, c=col: handle_button_click(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

# Create the reset button
reset_button = tk.Button(window, text='Reset', width=20, height=2, command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

# Start the main event loop
window.mainloop()
