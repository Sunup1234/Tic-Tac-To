import tkinter
import time

def check_Nul():
    global win
    if win is False:
        win = True
        print('Match Nul')


def print_winner():
    global win
    print('Le joueur ',current_player, 'a gagné')
    win = True


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = '0'
    else:
        current_player = 'X'


def check_win(clicked_row, clicked_col):

    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]

        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()

    count = 0
    for i in range(3):
        current_button = buttons[clicked_col][i]

        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()


    count = 0
    for i in range(3):
        current_button = buttons[i][i]

        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()

    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]

        if current_button["text"] == current_player:
            count += 1
    if count == 3:
        print_winner()

    if win is False:
       count = 0
       for col in range(3):
           for row in range(3):
               current_button = buttons[row][col]
               if current_button["text"] == 'X' or current_button["text"] == '0':
                   count += 1
       if count == 9 :
         print('Match Nul')


def place_symbol(row, column):
    if win is True:
        if not is_replaying:
            print('There is already a winner')
            return
    print("click", row, column)

    if not is_replaying:
        move_history.append((row, column))

    clicked_button = buttons[column][row]
    clicked_button.config(text=current_player)
    check_win(row, column)
    switch_player()

def reset_board():
    global current_player, win
    current_player = 'X'
    win = False
    for col in range(3):
        for row in range(3):
            buttons[col][row].config(text="")


def start_replay():
    global is_replaying

    if not move_history:
        print("No moves to replay yet.")
        return

    print("\n--- Starting Replay ---")
    is_replaying = True

    reset_board()
    root.update()
    time.sleep(0.5)

    for (r, c) in move_history:
        place_symbol(r, c)
        root.update()
        time.sleep(0.7)

    is_replaying = False
    print("--- Replay Finished ---\n")

def start_again():
    global current_player, win, move_history, is_replaying
    current_player = 'X'
    win = False
    move_history = []
    is_replaying = False

    for col in range(3):
        for row in range(3):
            buttons[col][row].config(text="")
            buttons[col][row].config(bg="SystemButtonFace")

            print("\n--- New Game Started ---")

def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root, font=("Arial",50),
                width=5, height=3,
                command= lambda r= row, c=column :place_symbol(r, c)
            )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

root = tkinter.Tk()
root.title("TIC TAC TO")
root.geometry("700x700")

buttons = []
move_history = []
current_player = 'X'
win = False
is_replaying = False

review_btn = tkinter.Button(root, text="Review Game", font=("Arial", 20), bg="lightblue", command=start_replay)
review_btn.grid(row=3, column=0, columnspan=3, sticky="NSEW")

replay_btn = tkinter.Button(root, text="Replay", font=("Arial", 20), bg="lightblue", command=start_again)
replay_btn.grid(row=4, column=0, columnspan=3, sticky="NSEW")


draw_grid()
root.mainloop()



