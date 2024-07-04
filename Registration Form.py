# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:29:27 2024

@author: madha
"""

import tkinter as tk
from tkinter import messagebox

def submit_form():
    Name = Name_entry.get()
    Email = Email_entry.get()
    Age = Age_entry.get() 
    Number =Number_entry.get() 
    Address = Address_entry.get()

    # You can add further validation or processing logic here
    # For now, let's display the entered data in a message box
    messagebox.showinfo("Registration Successful", f"Name: {name}\nEmail: {email}\nAge: {age}\nNumber: {number}\nAddress: {address}")

# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("900x700")

# Create form elements
name_label = tk.Label(root, text="Name :")
name_entry = tk.Entry(root)

email_label = tk.Label(root, text="Email :")
email_entry = tk.Entry(root)

age_label = tk.Label(root, text="Age :")
age_entry = tk.Entry(root)

number_label = tk.Label(root,text="Number : ") 
number_entry = tk.Entry(root) 

address_label = tk.Label(root, text="Addres :")
address_entry = tk.Entry(root)
  


submit_button = tk.Button(root, text="Submit", command=submit_form)

# Arrange form elements using grid layout
name_label.grid(row=0, column=0, padx=40, pady=20)
name_entry.grid(row=0, column=1, padx=40, pady=20)

email_label.grid(row=1, column=0, padx=40, pady=20)
email_entry.grid(row=1, column=1, padx=40, pady=20)

age_label.grid(row=2, column=0, padx=40, pady=20)
age_entry.grid(row=2, column=1, padx=40, pady=20) 

number_label.grid(row=3, column=0, padx=40, pady=20)
number_entry.grid(row=3, column=1, padx=40, pady=20) 

address_label.grid(row=4, column=0, padx=40, pady=20)
address_entry.grid(row=4, column=1, padx=40, pady=20) 

submit_button.grid(row=5, columnspan=3, padx=40, pady=30)

root.mainloop()
