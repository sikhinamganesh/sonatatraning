class Account:
    def __init__(self,account_no,name,type,balance):
        self.a=account_no
        self.b=name
        self.c=type
        self.d=balance
    def withdraw(self,amount):
        self.amount=amount
        return self.a, self.b, self.c, self.d,
