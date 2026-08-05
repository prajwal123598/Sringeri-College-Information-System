import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password


# Function to check password strength
def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength_label.config(text="Weak", fg="red")
    elif score == 3:
        strength_label.config(text="Medium", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")


# Function to generate password
def generate():
    try:
        length = int(length_entry.get())

        if length < 4:
            raise ValueError

        password = generate_password(length)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        check_strength(password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid password length (4 or more).")


# Function to copy password
def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first.")


# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("420x350")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

# Password Length
tk.Label(
    root,
    text="Password Length:",
    font=("Arial", 12)
).pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 12),
    justify="center"
)
length_entry.insert(0, "12")
length_entry.pack(pady=5)

# Generate Button
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    command=generate
)
generate_btn.pack(pady=10)

# Password Entry
password_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12),
    justify="center"
)
password_entry.pack(pady=5)

# Copy Button
copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=copy_password
)
copy_btn.pack(pady=10)

# Strength Label
tk.Label(
    root,
    text="Password Strength:",
    font=("Arial", 12)
).pack()

strength_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold")
)
strength_label.pack(pady=5)

# Developer Label
tk.Label(
    root,
    text="DEVELOPED BY PRAJWAL HM (BCA)",
    font=("Arial", 10, "italic"),
    bg="orange",
    fg="blue"
).pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()