#======================================================================
#                     Expense Tracker Project 2
#======================================================================

class Expense:

    def __init__(self , Expensename , catory , amount , date):
        self.Expensename = Expensename
        self.catory = catory
        self.amount = amount
        self.date = date
       


class ExpenseTracker:

    def __init__(self):
        self.expense = []

    def addExpense(self):

        Expensename = input("Enter Expense Name:\n")
        catory = input("Enter Expense Catory:\n")
        amount = float(input("Enter Amount:\n"))
        date = input("Enter date (DD/MM/YYYY):\n")

        expense = Expense(Expensename , catory , amount , date)

        self.expense.append(expense)

        print("Expense Added Successfully!")

    def viewExpense(self):

        if not self.expense:
            print("No Expense Found!")
            return

        for index , expense in enumerate(self.expense , start=1):

            
            print("----------- Expense List ----------")
            print("Expense ID:",index)
            print("Expense Name:",expense.Expensename)
            print("Catory:",expense.catory)
            print("Amount:",expense.amount)
            print("Date:",expense.date)
            print("------------------------------------")
    

    def deleteExpense(self):

        name = input("Enter Expense Name:\n")
        for expense in self.expense:

            if expense.Expensename.lower() == name.lower():
                self.expense.remove(expense)
                print("Expense Deleted Successfully!")
                return

        print("Expense Not Found!")

    def searchExpense(self):

        name = input("Enter Expense Name:\n")
        for expense in self.expense:

            if expense.Expensename.lower() == name.lower():
                
                print("----------- Search Expense ----------")
                print("Expense Name:",expense.Expensename)
                print("Catory:",expense.catory)
                print("Amount:",expense.amount)
                print("Date:",expense.date)
                print("-------------------------------------")
                return

        print("Expense Not Found!")


tracker = ExpenseTracker()

while True:

    print("======================================")
    print("            Expense Tracker           ")
    print("======================================")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Delete Expense")
    print("4. Search Expense")
    print("5. Exit")

    choice = input("Enter Choice:\n")

    if choice == "1":
        tracker.addExpense()

    elif choice == "2":
        tracker.viewExpense()

    elif choice == "3":
        tracker.deleteExpense()

    elif choice == "4":
        tracker.searchExpense()

    elif choice == "5":
        print("Exit Successfully!")
        break

    else:
        print("Invalid Choice , Try Again!")