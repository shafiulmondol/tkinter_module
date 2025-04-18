import tkinter
from tkinter import PhotoImage # for png formate image

root=tkinter.Tk()
root.geometry('500x500')
root.title('my app')
img_path=PhotoImage(file=r"C:\Users\MD SHAFIUL ISLAM\Downloads\download.png")
bg=tkinter.Label(root,image=img_path)
bg.place(relheight=1,relwidth=1)

text=tkinter.Label(root,text='welcome to my apps',font=('Georgia',24))
text.pack(pady=30)


root.mainloop()



# import tkinter
# from PIL import Image, ImageTk # for jpg formate image

# root = tkinter.Tk()
# root.geometry('500x500')
# root.title('My App')

# # Load the image using PIL
# img_path = r"C:\Users\MD SHAFIUL ISLAM\OneDrive\Pictures\download.jpg"
# image = Image.open(img_path)
# image = image.resize((500, 500), Image.ANTIALIAS)  # Resize the image if needed
# img_path = ImageTk.PhotoImage(image)

# # Set the image as background
# bg = tkinter.Label(root, image=img_path)
# bg.pack()

# root.mainloop()


