import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('300x300')
window.title("press button do stuff")


def showMsg():
    messagebox.showinfo('Message', 'You clicked the Submit button!')


button_border = tk.Frame(window, highlightbackground="black",
                         highlightthickness=1, bd=0,)


button = tk.Button(
    button_border,
    text="Click me!",
    width=25,
    height=5,
    bg="white",
    fg="black",
    border=1,
    command=showMsg
)

button.pack()
button_border.pack()

window.mainloop()
