import tkinter as tk
from tkinter import messagebox
from database import create_database
from expense_manager import ExpenseManager

class ExpenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Manager")
        
        self.root.geometry("400x400")
        
        self.root.configure(bg="#f0f8ff")
        
        self.manager = ExpenseManager()
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Amount:", bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(self.root, width=30)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Date:", bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(self.root, width=30)
        self.date_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Category:", bg="#f0f8ff").grid(row=2, column=0, padx=10, pady=10)
        self.category_entry = tk.Entry(self.root, width=30)
        self.category_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Description:", bg="#f0f8ff").grid(row=3, column=0, padx=10, pady=10)
        self.description_entry = tk.Entry(self.root, width=30)
        self.description_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Add Expense", command=self.add_expense, bg="#4CAF50", fg="white").grid(row=4, columnspan=2, padx=10, pady=10)
        tk.Button(self.root, text="View Expenses", command=self.view_expenses, bg="#2196F3", fg="white").grid(row=5, columnspan=2, padx=10, pady=10)

        self.expenses_list = tk.Listbox(self.root, width=50, height=10, bg="#ffffff")
        self.expenses_list.grid(row=6, columnspan=2, padx=10, pady=10)

    def add_expense(self):
        amount = self.amount_entry.get()
        date = self.date_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()

        if amount and date and category:
            self.manager.add_expense(amount, date, category, description)
            messagebox.showinfo("Success", "Expense added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    def view_expenses(self):
        self.expenses_list.delete(0, tk.END)
        expenses = self.manager.view_expenses()
        for expense in expenses:
            self.expenses_list.insert(tk.END, expense)

    def clear_entries(self):
        self.amount_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

if __name__ == "__main__":
    create_database() 
    root = tk.Tk()
    app = ExpenseApp(root)
    root.mainloop()
