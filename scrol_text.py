import tkinter
from tkinter import scrolledtext

root=tkinter.Tk()
root.geometry('500x500')
root.configure(background='skyblue')
root.title('create scrol text bar')

app_header=tkinter.Label(root,text='Welcome',font=('grick',24))
app_header.pack()
tect_scrol=scrolledtext.ScrolledText(root,wrap=tkinter.WORD,height=20,state=tkinter.DISABLED,bg='grey')
tect_scrol.pack(fill=tkinter.BOTH,expand=True,)
tect_scrol=scrolledtext.ScrolledText(root,wrap=tkinter.WORD,height=10)
tect_scrol.pack(fill=tkinter.BOTH,expand=True)

root.mainloop()