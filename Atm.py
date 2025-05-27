class ATM:
    def __init__(self, pin, balance=0):
        self.user_pin = pin
        self.balance = balance

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.user_pin:
                print("\nAuthentication successful.\n")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. Attempts remaining: {attempts}\n")
        print("Too many failed attempts. Exiting...")
        return False

    def display_menu(self):
        print("====== ATM Menu ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("=======================")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}\n")

    def deposit(self):
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}.\n")
        else:
            print("Invalid deposit amount.\n")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: $"))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ${amount:.2f}.\n")
        else:
            print("Insufficient funds or invalid amount.\n")

    def run(self):
        if not self.authenticate():
            return

        while True:
            self.display_menu()
            choice = input("Select an option (1-4): ")
            print()
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.\n")


# Example usage:
atm = ATM(pin="1234", balance=1000.00)
atm.run()
