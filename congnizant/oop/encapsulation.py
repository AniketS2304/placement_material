class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder     # Public
        self._balance = balance                  # Protected
        self.__pin = "1234"                      # Private

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount, pin):
        if pin == self.__pin:
            self._balance -= amount
        else:
            print("Wrong PIN!")

    def get_balance(self):
        return self._balance

acc = BankAccount("Aniket", 5000)
acc.deposit(1000)
print(acc.get_balance())  # ✅ Works
# print(acc.__pin)        # ❌ AttributeError
