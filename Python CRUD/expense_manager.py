import sqlite3

class ExpenseManager:
    def __init__(self):
        self.db_name = 'expenses.db'
    
    def add_expense(self, amount, date, category, description):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO expenses (amount, date, category, description) VALUES (?, ?, ?, ?)",
                  (amount, date, category, description))
        conn.commit()
        conn.close()
    
    def view_expenses(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM expenses")
        rows = c.fetchall()
        conn.close()
        return rows
