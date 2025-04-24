import tkinter
from tkinter import messagebox

root=tkinter.Tk()

root.geometry('300x400')
root.configure(background='skyblue')

def onclick():
    name=textbox1.get()
    email=textbox2.get()
    phon=textbox3.get()
    
    if name and email and phon:
        messagebox.showinfo('submited successfully')
    else:
        messagebox.showinfo('worning',' Fill the all field')
        

root.title("student regestation form")
lable1=tkinter.Label(root,text='Enter your name')
lable1.pack(anchor=tkinter.W,padx=10,pady=5)# w means west and pad means padding of x and y
textbox1=tkinter.Entry(root)
textbox1.pack(anchor=tkinter.W,padx=10,pady=5)

lable2=tkinter.Label(root,text='Enter your mail')
lable2.pack(anchor=tkinter.W,padx=10,pady=5)
textbox2=tkinter.Entry(root)
textbox2.pack(anchor=tkinter.W,padx=10,pady=5)

lable3=tkinter.Label(root,text='Enter your mobile')
lable3.pack(anchor=tkinter.W,padx=10,pady=5)
textbox3=tkinter.Entry(root)
textbox3.pack(anchor=tkinter.W,padx=10,pady=5)

submit_button=tkinter.Button(root,text='Submit',command=onclick)
submit_button.pack(anchor=tkinter.W,padx=10,pady=5)

root.mainloop()