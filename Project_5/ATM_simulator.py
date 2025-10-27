class ATM:
    def __init__(self, balance=1000):
        self._balance = balance

    def deposit(self):
        amount = float(input("How much would you like to deposit?\n"))
        if amount < 0:
            print("Cannot deposit negative value")
            return
        self._balance += amount
        print(f"Deposited {amount:.2f}, New balance: {self._balance:.2f}")

    def withdraw(self):
        amount = float(input("How much would you like to withdraw?\n"))
        if amount < 0:
            print("Cannot withdraw 0")
            return

        if amount > self._balance:
            print("Insufficient funds")
            return

        self._balance -= amount
        print(f"{amount:.2f} has been withdrawn, new balance is {self._balance:.2f}")

    def check_balance(self):
        print(f"your current balance is: {self._balance:.2f}")

    def run(self):
        while True:
            print("\n---ATM Menu---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            choice = input("Choose 1, 2, 3 or 4: ")

            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                print("Good Bye")
                break
            else:
                print("Invalid choice, try from 1 to 4")

if __name__ == "__main__":
    atm = ATM(balance=1000)
    atm.run()