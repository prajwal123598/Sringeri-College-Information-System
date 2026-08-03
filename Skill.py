from tkinter import *

root = Tk()
root.title("Address")
root.geometry("1000x1000")

def add(name):
    text.insert(END, f"{name}\n")
    text.insert(END, "Skill Center\n")
    text.insert(END, "Jay Street\n")
    text.insert(END, "Vayonapur 671290\n")
    text.insert(END, "-------------------------\n\n")

text = Text(root, width=40, height=15,bg='Green',fg='blue')
text.pack(pady=10)

add("Sonal")
add("Movin")
add("Sujal")

root.mainloop()