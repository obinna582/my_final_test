
import tkinter as tk
import random
from tkinter import messagebox

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Function to check the guess
def check_guess():
    try:
        guess = int(entry.get())
        if guess == secret_number:
            messagebox.showinfo("Result", "🎉 You guessed it! Well done!")
        else:
            messagebox.showinfo("Result", f"❌ Nope! The number was {secret_number}. Better luck next time!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Guess the Number Game")

# Add a label
label = tk.Label(window, text="I'm thinking of a number between 1 and 10.\nTake a guess:")
label.pack(pady=10)

# Add an entry box
entry = tk.Entry(window)
entry.pack(pady=5)

# Add a button to submit the guess
button = tk.Button(window, text="Submit Guess", command=check_guess)
button.pack(pady=10)

# Run the GUI loop
window.mainloop()

