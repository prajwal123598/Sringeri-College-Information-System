from tkinter import *

root = Tk()
root.title("My Window")
root.geometry("1000x800")

label = Label(root, text="Welcome", font=("Arial", 18), bg='Yellow',fg='blue')
label.pack(pady=20)

def show_hello():
    label.config(text="HELLOW USER", bg='White',fg='black')

def show_same():
    label.config(text="WELCOME ON",bg='orange',fg='red')

redbutton = Button(
    root,
    text="HELLO",
    fg="red",
    bg="orange",
    font=("Arial", 20, "bold"),
    command=show_hello
)

purplebutton = Button(
    root,
    text="REPLY",
    fg="purple",
    bg="green",
    font=("Arial", 20, "bold"),
    command=show_same
)

redbutton.pack(pady=10)
purplebutton.pack(pady=10)

root.mainloop()