import tkinter as tk

window = tk.Tk()
window.title("Cyber Security Health Checker")
window.geometry("600x400")

title = tk.Label(window, text="Hello World!", font=("Arial", 24))
title.pack(pady=40)

button = tk.Button(window, text="Click Me")
button.pack()

window.mainloop()