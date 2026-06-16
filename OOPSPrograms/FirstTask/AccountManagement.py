class AccountManagement:

    def __init__(self, name, account_no, email, debit_card):
        self.name = name
        self.account_no = account_no
        self.email = email
        self.debit_card = debit_card
        self.balance = 500  
        self.account_details = {
            "Name":self.name,
            "Account_no": self.account_no,
            "Email" : self.email,
            "Debit Card": self.debit_card,
            "Balance": self.balance
        }

    def account_holder_details(self):
        acc_holder = self.account_details
        print("\n--------- Your Account Details ---------")
        print(f"Name           : {acc_holder.get('Name')}")
        print(f"Account No     : {acc_holder.get('Account_no')}")
        print(f"Email          : {acc_holder.get('Email')}")
        print(f"Debit Card     : {acc_holder.get('Debit Card')}")
        print(f"Current Balance: {acc_holder.get('Balance')}")

    def check_bank_balance(self):
        print("\n--------- Bank Balance ---------")
        name = self.account_details['Name']
        balance = self.account_details['Balance']
        print(f"{name}, your current balance is {balance}")

    def deposit_money(self):
        amount = int(input("Enter amount to deposit: "))
        self.account_details["Balance"] += amount
        amount = amount+self.balance
        print(f"{amount} deposited successfully.")
        

    def withdraw_money(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            amount=self.balance-amount
            print(f"{amount} withdrawn successfully.")
            print(f"Updated Balance: {self.balance}")

    def loan_method(self):
        self.loan_amount=100000
        print("\n--------- Loan Application ---------")
        name = input("enter your name: ")
        age = int(input("Enter your age: "))
        work_exp = int(input("Enter your work experience (years): "))

        if age >= 30 and work_exp >= 5:
           
            print(f"Congratulations You are eligible for a bank loan of {self.loan_amount}") 
        else:
            print(" Sorry, you are not eligible for a bank loan.")


name = input("Enter Name: ")
account_no = int(input("Enter Account No: "))
email = input("Enter Email: ")
debit_card = input("Enter Debit Card No: ")

obj = AccountManagement(name, account_no, email, debit_card)

while True:
    print("\n---------------- MENU ----------------")
    print("1: View Account Details")
    print("2: Check Bank Balance")
    print("3: Deposit Money")
    print("4: Withdraw Money")
    print("5: Apply for a Loan")
    print("6: Exit")
    print("------------------------------------")

    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            obj.account_holder_details()
        case 2:
            obj.check_bank_balance()
        case 3:
            obj.deposit_money()
        case 4:
            obj.withdraw_money()
        case 5:
            obj.loan_method()
        case 6:
            print("Thank you for using the Bank Application ")
            break
        case _:
            print("Invalid choice! Please try again.")
