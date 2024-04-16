import mysql.connector as mysql # I don't understand why this is happening, "Defaulting to user installation because normal site-packages is not writeable...?"
# FIXED IT!! By creating a virtual environment I was able to identify that I had a $PATH conflict.

# Going to attempt & restore previous progress while handling with the bug later.

connection = mysql.connect(
    user = 'root',
    database = 'bank',
    password = '5G%m!^L8*40bM#rK$')


cursor = connection.cursor()

# Class = Pre-existing bank account that a user can access by checking the balance or depositing/withdrawing.
class BankAccount:
    def __intit__(self, account_number, pin, balance = 0):
        self.accountNumber = account_number
        self.pin = pin
        self.balance = balance
    
    def check_balance(self):
        return (f"Account {self.accountNumber} Balance: ${self.balance:.2f}")
    
    def deposit(self, amount):
        self.balance += amount

        return (f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
     
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return (f"Withdrew ${amount:.2f}. New Balnace: ${self.balance:.2f}")
        else:
            return ("Insufficient Funds.")

# Allows the user to create a new bank account of delete/modify a pre-existing one.
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, pin)
            return f"Account {account_number} created successfully."
        else:
            return "Account already exists."

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            return f"Account {account_number} closed successfully."
        else:
            return "Account not found."

    def modify_account(self, account_number, new_name, new_pin):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            account.pin = new_pin
            return f"Account {account_number} modified successfully."
        else:
            return "Account not found."

    
bank = Bank()
account_number = "12345"
pin = "1234"
bank.create_account(account_number, pin)
print(bank.accounts[account_number].check_balance())
print(bank.accounts[account_number].deposit(100))
print(bank.accounts[account_number].withdraw(50))
print(bank.close_account(account_number))







'''
testQuery = ("SELECT * FROM banker")
cursor.execute(testQuery)


for item in cursor:
    print(row)

cursor.close()
connection.close()
'''

def menu():
    print("--------Welcome to Sonic The Hedghog National Ring Bank--------")
    print("Press 1 To Sign In\nPress 2 To Sign Up\nPress 3 To Modify Or Delete An Account")

def choices():
    userInput = int(input("Select An Option: "))
    if userInput == 1:
        return(BankAccount)
    elif userInput == 2:
        return()

