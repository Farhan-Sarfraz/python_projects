
print("\n === ATM CHECKER SYSTEM === \n")

total_balance = 0
while True:
    print("1. Check balance: ")
    print("2. Deposit: ")
    print("3. Withdrawl: ")
    print("4. Exit: ")

    choice = input("Enter the choice. ")

    if choice == '1':
        print("Your balance is ", total_balance)
    elif choice == '2':
        amount = int(input("Enter the amount you want to deposit. "))
        total_balance += amount
        print("Your balance is now  ", total_balance)
    elif choice == '3':
        withdrawl_amount = int(input("Enter the amount you want to withdrawl. "))
        if withdrawl_amount > total_balance:
            print("Insufficient fund. ")
            
        else:
            total_balance -= withdrawl_amount
        print("Your current balance is ", total_balance)
    elif choice == '4':
        print("Thanks for joining us. ")
        break
    else:
        print("Invalid Choice. ")