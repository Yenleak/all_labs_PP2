class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def chel_balance(self):
        print(f"Balance is {self.balance}")
    
    def deposit(self, money):
        self.balance += money
        print({f"You are deposit {money} money"})
    
    def withdraw(self, money):
        if money > self.balance:
            print(print("Not enough money on balance"))
        else:
            self.balance -= money
            print(f"{money} has been withdrawn from deposit")

owner = Account("Yenlik",2500)
owner.chel_balance()
owner.deposit(2500)
owner.chel_balance()
owner.withdraw(2000)
owner.chel_balance()