# Expense Manager App

This repository contains a simple Expense Manager application built with Python and Tkinter. The app allows users to manage their expenses by adding, viewing, and storing them in a SQLite database.

## Features

- **Add Expense**: Enter details like amount, date, category, and description.
- **View Expenses**: Display all stored expenses in a list format.
- **Database Management**: Automatically creates a SQLite database to store expense records.

## Technologies Used

- Python
- Tkinter (for the GUI)
- SQLite (for database management)

## Installation

To run this application, make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## Code Overview
The code consists of three main components:

create_database: Initializes the SQLite database and creates the expenses table if it does not exist.
ExpenseManager: Handles the logic for adding and retrieving expenses from the database.
ExpenseApp: Manages the GUI using Tkinter and interacts with the ExpenseManager.

### Example of Database Schema
sql
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT
    );

## Resources
1. Python : [Python Tutorial](https://youtu.be/ix9cRaBkVe0?feature=shared).
2. Tkinter : [Tkinter Tutorial](https://youtube.com/playlist?list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T&feature=shared).
3. SQLite3: [SQLite3: Tutoria](https://youtu.be/Ykf5zxBMxZ8?feature=shared).
