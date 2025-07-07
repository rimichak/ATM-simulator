
def show_balance(balance):
    print(f"your balance is:{balance:.2f}")

def deposit():
    amount= float(input("Enter an amount to deposit:"))
    
    if amount < 0:
        print("The amount should be greater than 0")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdraw:"))

    if amount > balance:
        print("insufficient balance")
        return 0 
    elif amount < 0:
        print("The amount should be greater than 0")
        return 0
    else:
        return amount 
     
def main():

    balance = 50000
    while True:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
  
        choice = input("Enter your choice(1-4):")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            print("Exit! Have a nice day")
        else:
            print("No valid choices")

if __name__ == '__main__':
    main()