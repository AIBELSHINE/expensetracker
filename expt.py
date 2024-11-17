import tkinter as tk
from tkinter import ttk
import csv

# File to store data
FILE_NAME = "expenses.csv"

def add_expense():
    date = date_entry.get()
    description = description_entry.get()
    amount = amount_entry.get()
    category = category_combobox.get()

    if date and description and amount and category:
        # Save to file
        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, description, amount, category])
        load_expenses()
        clear_entries()

def load_expenses():
    for row in tree.get_children():
        tree.delete(row)

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                tree.insert("", tk.END, values=row)
    except FileNotFoundError:
        pass

def clear_entries():
    date_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_combobox.set("")

# GUI setup
root = tk.Tk()
root.title("Expense Tracker")

# Input Fields
tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1)

tk.Label(root, text="Description:").grid(row=1, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=1, column=1)

tk.Label(root, text="Amount:").grid(row=2, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1)

tk.Label(root, text="Category:").grid(row=3, column=0)
category_combobox = ttk.Combobox(root, values=["Food", "Transport", "Entertainment", "Other"])
category_combobox.grid(row=3, column=1)

add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=4, column=0, columnspan=2)

# Display Expenses
tree = ttk.Treeview(root, columns=("Date", "Description", "Amount", "Category"), show="headings")
tree.grid(row=5, column=0, columnspan=2)
tree.heading("Date", text="Date")
tree.heading("Description", text="Description")
tree.heading("Amount", text="Amount")
tree.heading("Category", text="Category")

load_expenses()
root.mainloop()
