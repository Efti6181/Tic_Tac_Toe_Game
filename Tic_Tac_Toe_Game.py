from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column]['text'] = player
        winner = check_winner()

        if winner:
            label.config(text=(winner + " wins"))
        elif not empty_spaces():
            label.config(text="Tie!")
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))

def check_winner():
    # Check rows and columns
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            highlight_winner([(i, 0), (i, 1), (i, 2)])
            return buttons[i][0]['text']
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            highlight_winner([(0, i), (1, i), (2, i)])
            return buttons[0][i]['text']

    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        highlight_winner([(0, 0), (1, 1), (2, 2)])
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        highlight_winner([(0, 2), (1, 1), (2, 0)])
        return buttons[0][2]['text']

    return None

def highlight_winner(cells):
    for row, col in cells:
        buttons[row][col].config(bg="green")

def empty_spaces():
    return any(buttons[row][col]['text'] == "" for row in range(3) for col in range(3))

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

# Initialize the game
window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0] for _ in range(3)]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()