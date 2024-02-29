class account:
    def _init_(self,balance):
        self.balance=balance
        self.min_balance=0

    def withdraw(self,amount):
        if ((self.balance-amount)>=self.min_balance):
            return amount
        else:
            return 0

class savingsaccount(account):
    def _init_(self,balance):
            account._init_(self,balance)
            self.min_balance=500

class currentaccount(account):
    def _init_(self,balance):
            account._init_(self,balance)
            self.min_balance=0

a1=savingsaccount(1000)
a2=currentaccount(1000)
account=[a1,a2]
for account in accounts:
    print(account.withdraw(1000))
