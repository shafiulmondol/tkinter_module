import tkinter
from tkinter import messagebox
from openpyxl import load_workbook

root = tkinter.Tk()
path = r"C:\Users\MD SHAFIUL ISLAM\OneDrive\문서\Book1.xlsx"

# Load the workbook and select the sheet
a = load_workbook(path)
# Replace 'Book1' with the actual sheet name if it's different
b = a['Sheet1']  # Change 'Sheet1' to your actual sheet name

root.title('Data Entry')
root.geometry('300x400')
root.configure(background='skyblue')

# Function to save the data to the Excel sheet
def save():
    n = name_entry.get()  # Use 'name_entry' to get the name input
    m = mail_entry.get()  # Use 'mail_entry' to get the email input
    p = phone_entry.get()  # Use 'phone_entry' to get the phone input

    # Check if all fields are filled
    if n and m and p:
        b.append([n, m, p])
        a.save(path)
        messagebox.showinfo('Successful', 'Data has been saved successfully!')
    else:
        messagebox.showinfo('Error', 'Please fill all the fields.')

# Create Labels and Entry widgets
name_label = tkinter.Label(root, text='Enter Name')
name_label.pack(anchor=tkinter.W, padx=10, pady=4)
name_entry = tkinter.Entry(root)
name_entry.pack(anchor=tkinter.W, padx=10, pady=4)

mail_label = tkinter.Label(root, text='Enter E-mail')
mail_label.pack(anchor=tkinter.W, padx=10, pady=4)
mail_entry = tkinter.Entry(root)
mail_entry.pack(anchor=tkinter.W, padx=10, pady=4)

phone_label = tkinter.Label(root, text='Enter Phone')
phone_label.pack(anchor=tkinter.W, padx=10, pady=4)
phone_entry = tkinter.Entry(root)
phone_entry.pack(anchor=tkinter.W, padx=10, pady=4)

# Create a Submit button
submit_button = tkinter.Button(root, text='Submit', command=save)
submit_button.pack(anchor=tkinter.W, padx=30, pady=4)

# Run the application
root.mainloop()
