class Account:
    def __init__(self, name):
        self.name = name
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.transactions = []
        self.balance = 0
        self.frozen = False
    def deposit(self, amount):
        if amount > 0:
            self.deposits.append(amount)
            self.transactions.append(f"Deposited: ${amount}")
            return f"Deposit successful. New balance: ${self.get_balance()}"

    def withdraw(self, amount):
        if amount > 0 and self.get_balance() - amount >= self.balance:
            self.withdrawals.append(amount)
            self.transactions.append(f"Withdrew: ${amount}")
            return f"Withdrawal successful. New balance: ${self.get_balance()}"

    def transfer_funds(self, amount, account):
        if self.get_balance() - amount >= self.balance:
            withdrawal_msg = self.withdraw(amount)
            deposit_msg = account.deposit(amount)
            self.transactions.append(f"Transferred: ${amount} to {account.name}")
            return f"Transfer successful. {withdrawal_msg}"
 
    def get_balance(self):
        return sum(self.deposits) - sum(self.withdrawals)
    def get_loan(self, amount):
        if amount>0:
            self.loan += amount
        return f"You requested a loan of {amount}"

    def repay_loan(self, amount):
        if amount > 0:
            if amount >= self.loan:
                self.transactions.append(f"Loan Repaid: ${self.loan}")
                self.loan = 0
            else:
                self.loan -= amount
                self.transactions.append(f"Partial Loan Repayment: ${amount}")
            return f"Loan repayment successful. Remaining loan: ${self.loan}"

    def view_account_details(self):
        return f"Account Owner: {self.name}\nBalance: ${self.get_balance()}\nLoan: ${self.loan}"
       
    def account_statement(self):
        print("Account Statement:")
        for transaction in self.transactions:
            print(transaction)
        print(f"Current Balance: ${self.get_balance()}")

    def apply_interest(self):
        interest = self.get_balance() * 0.05
        self.deposits.append(interest)
        self.transactions.append(f"Interest Applied: ${interest}")
        return f"Interest of ${interest} applied. New balance: ${self.get_balance()}"

    def minimum_balances(self, amount):
        if amount >= 0:
            self.minimum_balance = amount
            return f"Minimum balance set to ${amount}"
    
    def freeze(self):
        self.frozen = True
        return f"Account has been frozen for security reason"
        
    def un_freeze(self):
        self.frozen = False
        return f"Account has been unfrozen"
        
    def close_account(self):
        self.balance = 0
        self.deposits.clear()
        self.withdrawals.clear()
        self.loan.clear()
        self.transaction.clear()
        self.min_balance = 0
        

account=Account("Jane")     
print(account.deposit(2000))
print(account.withdraw(1000))
print(account.transfer_funds(2000,"Bk account"))
print(account.get_balance())
print(account.get_loan(5000))
print(account.repay_loan(3000))
print(account.view_account_details())
print(account.account_statement())
print(account.apply_interest())
print(account.minimum_balances(3000))
print(account.freeze())
print(account.un_freeze())

