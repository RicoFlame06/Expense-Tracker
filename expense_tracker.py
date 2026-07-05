
expenses = []

def menu():

    print("")

    print("Welcome to the Expense Tracker")

    print("1: Add Expenses")
    print("2: View Expenses")
    print("3: View Total Spent")
    print("4: Exit")

    print("")

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

            expense = [itemName, price, category]  # New list to make seperate lists possible inside expenses list

            expenses.append(expense) # New list added to the original list

            print("Items Added!")
                
            break

            
        except ValueError:

            print("Invalid Input")

  




def viewExpenses(): # Views each expense (reciept)

    print("Current Expenses:")   

    for expense in expenses: #Iterates and loops through expenses for expense lists

        print("")

        print("Item Name: ",expense[0])
        print("Price: ",expense[1])
        print("Category: ",expense[2])

        print("")



def getTotalSpent():
             
    total = 0

    for expense in expenses:

        total = total + expense[1]

    print("Total Spent: ")

    print("£", total)



             
          
  
while True: # Continues after user completes an option


    userOption = menu()


    if userOption == 1:

        addExpenses()


    elif userOption == 2:

        viewExpenses()

    elif userOption == 3:

        getTotalSpent()

    else:
        print("Goodbye")
        break


