from tkinter import *

root = Tk()
root.geometry("300x200")  # width x height

# Use a proper font name and apply italic styling correctly
l = Label(root, text="Shafiul", font=("Arial", 10, "bold italic"))
l.pack()

root.mainloop()
