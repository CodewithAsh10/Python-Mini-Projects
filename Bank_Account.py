class Bank_Account:
    def __init__(self,balance=0):
        self.balance = balance
        
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposit Successful ! New Balance: {self.balance}")
        else:
            print("Please enter a valid amount")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds ! ")
        elif amount<=0:
            print("Please enter the valid amount")
        else:
            self.balance-=amount
            print(f"Withdraw successful! New Balance: {self.balance}")
    def check_balance(self):
        print(f"Current Balance: {self.balance}")
def bank_menu():
    account = Bank_Account(1000)
    while True:
        print("\nBank Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Ckeck Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice=="1":
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice=="2":
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice=="3":
            account.check_balance()
        elif choice=="4":
            print("Exiting.... Thank You!")
            break
        else:
            print("Invalid Choice")
bank_menu()

        