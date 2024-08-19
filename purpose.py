import tkinter as tk
import random

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Popup")
    label = tk.Label(popup, text="Thanks for Accepting my purposal" , font=("Arial", 24), background="lightblue")
    label.pack(padx=30, pady=30)

def move_button(event):
    x = random.randint(0, 350)
    y = random.randint(0, 350)
    no_button.place(x=x, y=y)

root = tk.Tk()
root.title("Love Request purpose")
root.geometry("400x400")

question_label = tk.Label(root, text="Do you love me?",font=("Arial", 40), background="lightblue")
question_label.pack(pady=20)

yes_button = tk.Button(root, text="Yes",background="green",font=("Arial", 24) , command=show_popup)
yes_button.pack()

no_button = tk.Button(root, text="No",background="red", font=("Arial", 24))
no_button.pack()

no_button.bind("<Enter>", move_button)

root.mainloop()