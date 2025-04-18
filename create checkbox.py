import tkinter
from tkinter import ttk

root=tkinter.Tk()
root.geometry('400x300')

def main():
    print(agree.get())

agree=tkinter.IntVar() # if checkbox is right value is 1 otherwise 0
agree_check=ttk.Checkbutton(root,text="Do you agree with this terms and conditions?",variable=agree)
agree_check.pack()

submit=tkinter.Button(root,text='submit',command=main)
submit.pack()

root.mainloop()