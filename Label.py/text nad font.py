from tkinter import *

root = Tk()
root.geometry("500x500")
root . title("Text and Font")
label = Label(
    root,
    text="Shafiul islam",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="blue",
    width=20,
    height=3,
    padx=10,
    pady=5,
    relief="ridge",
    bd=5,
    anchor="center",
    cursor="hand2"
)
label.pack()

root.mainloop()
