
expenses = ["toy", 5, "fun"]

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

    while True:

        try:

                itemName = input("Item Name: ")

                price = int(input("Price: "))

                category = input("Category: ")

                expense = [itemName, price, category] 
                expenses.append(expense)

                print("Items Added!")
                
                break

            
        except ValueError:

            print("Invalid Input")




def viewExpenses():
        
        for i in expenses:
            print(i)




  
while True: # Continues after user completes an option


    userOption = menu()


    if userOption == 1:

        addExpenses()


    elif userOption == 2:

        viewExpenses()




