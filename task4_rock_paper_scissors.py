import tkinter as tk
from tkinter import messagebox
import random
	
user_points = 0
computer_points = 0
winning_score = 10 

def determine_winner(user_choice, computer_choice):
    global user_points
    global computer_points
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        user_points += 1
        return "You win!"
    else:
        computer_points += 1
        return "Computer wins!"

def user_choice(choice):
    if user_points < winning_score and computer_points < winning_score:
        computer_choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(computer_choices)

        result = determine_winner(choice, computer_choice)

        result_label.config(text=f"Computer chose: {computer_choice}\n{result}",fg='black', bg='light green',)

        score_label.config(text=f"Your Score: {user_points}  Computer Score: {computer_points}",fg='black', bg='grey',)

        if user_points >= winning_score:
            messagebox.showinfo("Game Over", "You win the game!")
            reset_game()
        elif computer_points >= winning_score:
            messagebox.showinfo("Game Over", "Computer wins the game!")
            reset_game()

def reset_game():
    global user_points
    global computer_points
    
    user_points = 0
    computer_points = 0
    
    instruction_label.config(text="Choose Rock, Paper, or Scissors:",fg='black', bg='light green',)
    result_label.config(text="",fg='black', bg='red',)
    score_label.config(text="Your Score: 0  Computer Score: 0",fg='black', bg='grey',)

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("375x350")
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:",fg='black', bg='light green')
instruction_label.pack()

rock_button = tk.Button(root, text="Rock",fg='black', bg='white', command=lambda: user_choice("Rock"))
paper_button = tk.Button(root, text="Paper",fg='black', bg='white', command=lambda: user_choice("Paper"))
scissors_button = tk.Button(root, text="Scissors",fg='black', bg='white', command=lambda: user_choice("Scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

result_label = tk.Label(root, text="",fg='black', bg='grey', font=("Comic Sans MS", 18, "bold"))
result_label.pack()

score_label = tk.Label(root, text="Your Score: 0  Computer Score: 0",fg='black', bg='light green', font=("Comic Sans MS", 12, "bold"))
score_label.pack()

play_again_button = tk.Button(root, text="Reset Game",fg='black', bg='grey', command=reset_game)
play_again_button.pack()
root.mainloop()
