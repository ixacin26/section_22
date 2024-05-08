from datetime import datetime

class Bank:
    #setting the initial amount with a default value of zero
    def __init__(self, starting_balance=0):
        self.balance = starting_balance
        print(f"Starting balance is {starting_balance}")
        f = open("saldo.txt", "a")
        f.write(f"{datetime.now()}\t\t\tStarting Balance: {starting_balance}\n")
        f.close()
    #writing to an external file
    def transaction_log(self, transaction):
        f = open("saldo.txt", "a")
        f.write(transaction)
        f.close()
    #depositing amount
    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.transaction_log(f"{datetime.now()}\t\t\tDeposit: {amount}\t\t\tBalance: {account.balance}\n")
            print("Deposit was successful!")

    #withdrawing amount
    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.transaction_log(f"{datetime.now()}\t\t\tWithdrawal: {amount}\t\t\tBalance: {account.balance}\n")
            print("Withdrawal was successful!")

# Start of operating code

while True:
    while True:
        try:
            initial_balance = float(input("What is the inital balance? "))
            break
        except ValueError:
            print("This is not a valid number - please use only numbers and no comma")

    account = Bank(initial_balance)

    while True:
        
        transaction = ""
        while transaction not in ["d", "w"]:
            transaction = input("Do you want to deposit (d) or withdraw (w) money? ")

            if transaction not in ["d", "w"]:
                print("Please choose (d) for deposit and (w) for withdrawal")

        #deal with deposits    
        if transaction == "d":
            amount = input("How much do you want to deposit? ")
            account.deposit(amount)
            print(f"{datetime.now()}\t\t\tDeposit: {amount}\t\t\tBalance: {account.balance}")
        else:
            amount = input("How much do you want to withdraw? ")
            account.withdrawal(amount)
            print(f"{datetime.now()}\t\t\tWithdrawal: {amount}\t\t\tBalance: {account.balance}")

        #asking the user if he wants to continue or leave
        next_transaction = input("Press any key for another transaction or 'n' for ending your banking session: ")

        if next_transaction == "n":
            break

    break
    