import tkinter
from tkinter import messagebox,ttk
import openpyxl


root=tkinter.Tk()
root.geometry('300x400')
root.configure(background='skyblue')



bran=tkinter.Label(root,text='Enter your choices')
bran.pack(anchor=tkinter.W,padx=10,pady=4)
choices=['CS','EC','MECHAMICAL']
brance_drop=ttk.Combobox(root,values=choices)
brance_drop.pack(anchor=tkinter.W,padx=10,pady=4)

submit_button=tkinter.Button(root,text='Submit')
submit_button.pack(anchor=tkinter.W,padx=30,pady=4)
root.mainloop()