# greetings, {name}      --- USE the + method
# variables: Current balance
# basic operators: add income; subtract expenses
# lists: store expenses and income as strings
# Display CURRENT BALANCE; TRANSACTION HISTORY CLEANLY

# FEATURES:
# User inputs initial balance (E.g. $3000)
# add income; subtract expenses
# Store each transaction: "Added $20"; "Spent $15" IN A LIST
# AFTER EACH TRANSACTION: print formatted current balance, last transaction
# Exit when user types "exit"
# After typing exit, pring the entire transaction history, EACH ON THE NEW LINE

user = str(input("Enter your name: "))
print("Greetings, " + user)

initial_balance = int(input("Input your current balance(numbers only): "))
balance = initial_balance

print("Current balance: ", balance)

amount_list = []

while True:
    income_expense = str(input("Income and expense(+/-): "))
    if income_expense == "exit":
        print("\nTransaction History:")
        for income_expense in amount_list:
            print(income_expense)
        print(f"Final balance: {balance}")
        exit()

    amount = int(input("Amount?: "))

    if income_expense == "+":
        balance += amount
        amount_list.append(amount)
        print(f"+${amount}")

    elif income_expense == "-":
        balance -= amount
        amount_list.append(-amount)
        print(f"-${amount}")

    else:
        print("Invalid input, use + or -")

    print(f"Current balance: {balance}")
    print("Transaction history:", amount_list)
