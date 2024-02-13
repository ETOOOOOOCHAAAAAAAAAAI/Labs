class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Новый баланс:", self.balance)


    def withdraw(self, amount):
        if amount > self.balance:
            print("На счету недостаточно средств.")
        else:
            self.balance -= amount
            print(f"Выведено ${amount}.Новый баланс ${self.balance}.")

acc = Account("AHAHAHAHAHAHAHHA")
acc.deposit(100)
acc.deposit(50)
acc.withdraw(20)
acc.withdraw(150)