# Represents a single bank account (one customer).
# Stores the owner's name and their account balance.
class bank_account:
    def __init__(self, owner, balance):
        # Initialize the account with an owner and a starting balance.
        self._owner = owner
        self._balance = balance

    # Add money to the account
    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount must be positive.")
        if amount > 0:
            # Increase balance by the deposit amount
            self._balance += amount

    # Withdraw money from the account
    def withdraw(self, amount):
        if amount > self._balance:
            # Prevent overdrawing
            print("Insufficient funds")
        elif amount <= self._balance:
            # Decrease balance if there is enough money
            self._balance -= amount

    # Return the current account balance
    def get_balance(self):
        return self._balance


# Represents the bank itself.
# Manages multiple bank accounts using a dictionary.
class bank:
    def __init__(self):
        # Dictionary to store accounts, where:
        # key = owner's name, value = bank_account object
        self._account = {}

    # Create a new account and add it to the bank
    def create_account(self, owner, balance=0):
        new_account = bank_account(owner, balance)
        # Store the new account using the owner's name as the key
        self._account[owner] = new_account

    # Find and return an existing account by owner's name
    def find_account(self, owner):
        if owner in self._account:
            return self._account[owner]
        else:
            print("No such account exists")
            return None

    # (Unused in this version)
    # Could be used to return the balance of a single account
    def get_balance(self):
        return self._balance

    # Calculate the total money held across all accounts in the bank
    def total_holdings(self):
        total = 0
        # Loop through all account objects and sum their balances
        for item in self._account.values():
            total += item.get_balance()
        return total

    # Return a nicely formatted string with all accounts and total holdings
    def __str__(self):
        # If the bank has no accounts yet
        if not self._account:
            return "no accounts in the bank"

        # Start building a list of output lines
        output = ["Bank accounts: "]
        # Add each account's owner and their current balance
        for owner, account in self._account.items():
            output.append(f" {owner}: {account.get_balance()}")
        # Add total holdings at the bottom
        output.append(f"total holdings: {self.total_holdings()}")

        # Join all lines with line breaks and return as a single string
        return "\n".join(output)


if __name__ == "__main__":
    # Create a new bank instance
    my_bank = bank()

    # Create three new accounts
    my_bank.create_account("Alice", 500)
    my_bank.create_account("Bob", 300)
    my_bank.create_account("Charlie", 1000)

    # Print all accounts and their balances
    print("=== Initial Bank State ===")
    print(my_bank)
    print()

    # Deposit 200 into Bob's account
    account = my_bank.find_account("Bob")
    if account:
        account.deposit(200)

    # Withdraw 100 from Alice's account
    account = my_bank.find_account("Alice")
    if account:
        account.withdraw(100)

    # Try to withdraw more money than Charlie has
    account = my_bank.find_account("Charlie")
    if account:
        account.withdraw(2000)

    # Print the updated state of all accounts
    print("\n=== Final Bank State ===")
    print(my_bank)
