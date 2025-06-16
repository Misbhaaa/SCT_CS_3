import tkinter as tk
from tkinter import messagebox
import re

def check_strength(password):
    feedback = []
    
    if len(password) < 6:
        feedback.append("Too short (min 6 characters).")
    if re.search(r"[a-z]", password) is None:
        feedback.append("Missing lowercase letters.")
    if re.search(r"[A-Z]", password) is None:
        feedback.append("Missing uppercase letters.")
    if re.search(r"\d", password) is None:
        feedback.append("Missing digits.")
    if re.search(r"[^A-Za-z0-9]", password) is None:
        feedback.append("Missing special characters.")

    score = 5 - len(feedback)

    if score == 5 and len(password) >= 12:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback

def evaluate():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password")
        return
    
    strength, feedback = check_strength(password)
    result_text = f"Password Strength: {strength}"
    
    if feedback:
        result_text += "\n\nSuggestions:\n- " + "\n- ".join(feedback)

    result_label.config(text=result_text)

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Password Strength Checker")
root.resizable(False, False)

window_width = 550
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=35, font=("Arial", 12), justify="center")
entry.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Check Strength", command=evaluate, font=("Arial", 12)).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Clear", command=clear, font=("Arial", 12)).grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 11), fg="blue", justify="left")
result_label.pack(padx=20)

root.mainloop()
