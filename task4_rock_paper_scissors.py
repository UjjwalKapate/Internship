import tkinter as tk
from tkinter import ttk
import random

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to update the game result label
def update_result():
    user_choice = user_var.get()
    computer_choice = random.choice(choices)
    computer_var.set(computer_choice)

    result = determine_winner(user_choice, computer_choice)
    result_var.set(result)

# Create the main application window
app = tk.Tk()
app.title("Rock, Paper, Scissors Game")

# Create a label for instructions
instruction_label = tk.Label(app, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14))
instruction_label.pack(pady=10)

# Create a Combobox for user's choice
choices = ["Rock", "Paper", "Scissors"]
user_var = tk.StringVar()
user_choice_combobox = ttk.Combobox(app, textvariable=user_var, values=choices, font=("Helvetica", 14), state="readonly")
user_choice_combobox.pack(pady=10)
user_choice_combobox.set("Rock")

# Create a button to play the game
play_button = ttk.Button(app, text="Play", command=update_result)
play_button.pack(pady=10)

# Create a label to display computer's choice
computer_var = tk.StringVar()
computer_label = tk.Label(app, textvariable=computer_var, font=("Helvetica", 14))
computer_label.pack(pady=10)

# Create a label to display the game result
result_var = tk.StringVar()
result_label = tk.Label(app, textvariable=result_var, font=("Helvetica", 16), wraplength=300)
result_label.pack(pady=10)

# Run the application
app.mainloop()