import tkinter as tk

window = tk.Tk()
window.title("Length Converter App")
window.geometry("400x400")

def check_strength():
    password = entry.get()
    length = len(password)

    if length <= 5:
        strength_label.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        strength_label.config(text="Medium", fg="yellow")
    elif 9 <= length <= 12:
        strength_label.config(text="Strong", fg="light green")
    else:
        strength_label.config(text="Very Strong", fg="dark green")

title_label = tk.Label(
    window,
    text="Password Strength Checker",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=20)

entry_label = tk.Label(
    window,
    text="Enter Password:",
    font=("Arial", 12)
)
entry_label.pack(pady=5)

entry = tk.Entry(window, show="*", font=("Arial", 12))
entry.pack(pady=5)

check_button = tk.Button(
    window,
    text="Check Strength",
    font=("Arial", 12),
    bg="#3498db",
    fg="white",
    command=check_strength
)
check_button.pack(pady=15)

strength_label = tk.Label(
    window,
    text="",
    font=("Arial", 14, "bold")
    )
strength_label.pack(pady=10)

window.mainloop()
