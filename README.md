no#  DecodeLabs Expense Tracker

> A terminal-based personal expense management application built with Python — Task 2

---

## Overview

The **DecodeLabs Expense Tracker** is a command-line application designed to help users record and manage their daily expenses. It allows you to add expenses with category and amount details, view the full expense list, search for a specific expense by name, and delete entries — all through a clean interactive menu.

---

##  Features

-  **Add Expense** — Log an expense with its name, category, amount, and date
-  **View Expenses** — Display all recorded expenses with numbered IDs
-  **Search Expense** — Find a specific expense by name instantly
-  **Delete Expense** — Remove an expense entry by name
-  **Interactive Menu Loop** — Keeps running until the user chooses to exit

---

## Tech Stack

| Technology | Details         |
|------------|-----------------|
| Language   | Python 3.13.5    |
| Paradigm   | Object-Oriented Programming |
| Interface  | Command-Line Interface   |
| Libraries  | (Built-In) |

---

##  Project Structure

```
DecodeLabs-Expense-Tracker/
│
├── expense_tracker.py    # Main application file
└── README.md             # Project documentation
```

---

##  How to Run

### Prerequisites

- Python 3.13.5 installed on your system

### Steps

```bash
# 1. Clone or download the project
git clone https://github.com/your-username/decodelabs-expense-tracker.git

# 2. Navigate into the project folder
cd decodelabs-expense-tracker

# 3. Run the application
python expense_tracker.py
```

---

##  Usage

Once the program runs, you'll see the following menu:

```
======================================
            Expense Tracker
======================================
1. Add Expense
2. View Expense
3. Delete Expense
4. Search Expense
5. Exit
```

### Example Workflow

**Adding an Expense:**
```
Enter Choice: 1
Enter Expense Name: Grocery
Enter Expense Category: Food
Enter Amount: 1500
Enter Date (DD/MM/YYYY): 15/06/2025
Expense Added Successfully!
```

**Viewing Expenses:**
```
----------- Expense List ----------
Expense ID: 1
Expense Name: Grocery
Category: Food
Amount: 1500.0
Date: 15/06/2025
------------------------------------
```

**Searching an Expense:**
```
Enter Choice: 4
Enter Expense Name: Grocery
----------- Search Expense ----------
Expense Name: Grocery
Category: Food
Amount: 1500.0
Date: 15/06/2025
-------------------------------------
```

**Deleting an Expense:**
```
Enter Choice: 3
Enter Expense Name: Grocery
Expense Deleted Successfully!
```

---

## Class Design

### `Expense`
Represents a single expense record.

| Attribute      | Type    | Description                            |
|----------------|---------|----------------------------------------|
| `Expensename`  | `str`   | Name of the expense                    |
| `catory`       | `str`   | Category the expense belongs to        |
| `amount`       | `float` | Cost of the expense                    |
| `date`         | `str`   | Date of the expense (DD/MM/YYYY)       |

---

### `ExpenseTracker`
Manages the full list of expense records.

| Method            | Description                                      |
|-------------------|--------------------------------------------------|
| `addExpense()`    | Takes input and adds a new `Expense` to the list |
| `viewExpense()`   | Prints all expenses with numbered IDs            |
| `deleteExpense()` | Finds and removes an expense by name             |
| `searchExpense()` | Finds and displays a specific expense by name    |

---



## Author

**DecodeLabs — Task 2**

> Built as part of the DecodeLabs Python learning series.

---

##  License

This project is open-source and free to use for educational purposes.
