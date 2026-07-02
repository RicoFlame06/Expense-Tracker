

def expenseTracker():

    def expensesList():
        expenses = []
        return expenses        

    def menu():

        print("Welcome to the Expense Tracker")

        print("1: Add Expenses")
        print("2: View Expenses")
        print("3: View Total Spent")
        print("4: Exit")

        while True:
        
            try:
                user_option = int(input("Pick options 1-4: "))
                return user_option

            except ValueError:
                print("Enter number 1-4")




    def addExpenses(): 

        expenses = expensesList()

        while True:

            try:

                itemName = input("Item Name: ")
                expenses.append(itemName)

                price = int(input("Price: "))
                expenses.append(price)

                category = input("Category: ")
                expenses.append(category)

                print("Items Added!")

                print(expenses)

                return expenses
            
            except ValueError:

                print("Invalid Input")




    def viewExpenses():
        expenses = addExpenses()
        print(expenses)


    def viewTotalSpent():
        expenses = addExpenses()

        expenses[2]

    userOption = menu()


    if userOption == 1:

        addExpenses()


    elif userOption == 2:

        viewExpenses()


expenseTracker()


