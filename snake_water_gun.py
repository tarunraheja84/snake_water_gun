import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Snake Water Gun Game")

# Define the moves and images
moves = ["Snake", "Water", "Gun"]
snake_img = tk.PhotoImage(file=r"C:\Users\tarun\Desktop\snake.png").subsample(4, 4)
water_img = tk.PhotoImage(file=r"C:\Users\tarun\Desktop\water.png").subsample(4, 4)
gun_img = tk.PhotoImage(file=r"C:\Users\tarun\Desktop\gun.png").subsample(2, 2)

# Define the game logic
def play_game(player_choice):
    computer_choice = random.choice(moves)
    result = ""

    if player_choice == computer_choice:
        result = "Tie"
    elif player_choice == "Snake":
        if computer_choice == "Water":
            result = "Win"
        else:
            result = "Lose"
    elif player_choice == "Water":
        if computer_choice == "Gun":
            result = "Win"
        else:
            result = "Lose"
    elif player_choice == "Gun":
        if computer_choice == "Snake":
            result = "Win"
        else:
            result = "Lose"

    result_label.config(text=f"You {result}! Computer chose {computer_choice}.")

# Create the GUI elements
title_label = tk.Label(root, text="Choose your move:")
title_label.pack(pady=10)

moves_frame = tk.Frame(root)
moves_frame.pack()

snake_button = tk.Button(moves_frame, image=snake_img, command=lambda: play_game("Snake"))
snake_button.pack(side="left", padx=10)

water_button = tk.Button(moves_frame, image=water_img, command=lambda: play_game("Water"))
water_button.pack(side="left", padx=10)

gun_button = tk.Button(moves_frame, image=gun_img, command=lambda: play_game("Gun"))
gun_button.pack(side="left", padx=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Run the GUI
root.mainloop()
