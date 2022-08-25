class Account:
    def __init__(self,accno,name,acctype,bal):
        self.account_number=accno
        self.username=name
        self.accounttype=acctype
        self.balance=bal
    def withdraw(self,amount):
        self.amt=amount
        if(self.balance<self.amt):
            return 'LowBalanceException'



