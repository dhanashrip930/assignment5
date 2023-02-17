class Account:
    def __init__(self,title=0,balance=0):
        self.title=title
        self.balance=balance

class SavingAccount(Account):
    def __init__(self,title,balance,interestRate):
        self.interestRate=interestRate
        super(). __init__(title,balance)

    def display(self):
        return(f"{self.title} is the title ,and  {self.balance} is the balance,and {self.interestRate} is the interestRate")


obj=SavingAccount("Ashish",5000,5) 
print(obj.display())
