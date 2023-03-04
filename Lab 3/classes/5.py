class Bank:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance 

    def deposit(self, dep):
        self.dep = dep
        self.balance += self.dep

    def withdraw(self, take):
        self.take = take
        if self.balance-self.take <=0:
            print("You have not enough balance!")
        else:
            print("Balance now:", self.balance-self.take)

print("Enter your name: ")
bank = Bank(input(), 1500000)
print(bank.owner, "Balance:", bank.balance)
bank.deposit(int(input("Enter deposit amount: ")))
bank.withdraw(int(input("Enter withdrawal amount: ")))
