class Account:
    def __init__(self,balance,account_number):
        self.balance=balance
        self.account_number=account_number
    def debit(self,amount):
        self.balance-=amount
        print("rs.", amount,"was debited")
        print("balance left:",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("rs.",amount,"was credited")
        print("balance left :", self.get_balance())
        
    def get_balance(self):
        return self.balance
emp1=Account(10000,1245698)
emp1.debit(6000)
emp1.credit(8000)
