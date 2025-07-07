balance = 50000
Running = True

def show_balance():
    print(f"your balance is:{balance:.2f}")

def deposit():
    amount= float(input("Enter an amount to deposit:"))
    
    if amount < 0:
        print("The amount should be greater than 0")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to be withdraw:"))

    if amount > balance:
        print("insufficient balance")
        return 0 
    elif amount < 0:
        print("The amount should be greater than 0")
        return 0
    else:
        return amount   


while Running:
    print("Choices")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your choice(1-4):")

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        Running = False
    else:
        print("No valid choices")