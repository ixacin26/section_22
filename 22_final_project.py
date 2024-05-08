from datetime import datetime

#defining the starting balance
balance = 0

while True:
    
    transaction = ""
    while transaction not in ["d", "w"]:
        transaction = input("Do you want to deposit (d) or withdraw (w) money? ")

        if transaction not in ["d", "w"]:
            print("Please choose (d) for deposit and (w) for withdrawal")

    #deal with deposits    
    if transaction == "d":
        while True:
            deposit = input("How much do you want to deposit? ")
            try:
                float(deposit)
                break
            except ValueError:
                print("This is not a valid input - please only use numbers!")

        print(f"Your deposit of {deposit} was successful!")
        balance += float(deposit)
        
        print(f"{datetime.now()}\t\t\tDeposit: {deposit}\t\t\tSaldo: {balance}")
        f = open("saldo.txt", "a")
        f.write(f"{datetime.now()}\t\t\tDeposit: {deposit}\t\t\tSaldo: {balance}\n")
        f.close()

    #deal with withdrawls
    if transaction == "w":
        while True:
            withdrawl = input("How much do you want to withdrawl? ")
            try:
                float(withdrawl)
                break
            except ValueError:
                print("This is not a valid input - please only use numbers!")

        print(f"Your withdrawl of {withdrawl} was successful!")
        balance -= float(withdrawl)

        #Print to external file and on console
        print(f"{datetime.now()}\t\t\tWithdrawl: {withdrawl}\t\t\tSaldo: {balance}")
        f = open("saldo.txt", "a")
        f.write(f"{datetime.now()}\t\t\tWithdrawl: {withdrawl}\t\t\tSaldo: {balance}\n")
        f.close()

    #asking the user if he wants to continue or leave
    next_transaction = input("Press any key for another transaction or 'n' for ending your banking session: ")

    if next_transaction == "n":
        break
    