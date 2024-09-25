from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player
        buttons[row][column].config(bg="red" if player == "X" else "blue")  # Set color based on player

        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))
        elif check_winner() is True:
            label.config(text=(player + " wins!"))
        elif check_winner() == "Tie":
            label.config(text=("It's a tie!"))

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            for col in range(3):
                buttons[row][col].config(bg="green")  # Winning row turns green
            return True
            
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            for row in range(3):
                buttons[row][column].config(bg="green")  # Winning column turns green
            return True
            
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        for i in range(3):
            buttons[i][i].config(bg="green")  # Winning diagonal turns green
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        for i in range(3):
            buttons[i][2 - i].config(bg="green")  # Winning diagonal turns green
        return True

    if empty_box() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")  # Tie condition
        return "Tie"

    return False

def empty_box():
    return any(button['text'] == "" for row in buttons for button in row)

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")  # Reset button text and color

# Create the main window
window = Tk()
window.title("Tic Tac Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Label to display the current player or the game result
label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

# Reset button to start a new game
reset_button = Button(text="Reset", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

# Frame for the game buttons
frame = Frame(window)
frame.pack()

# Create the game buttons
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)
        buttons[row][column].config(bg="#F0F0F0")  # Set default background color

# Start the main loop
window.mainloop()


