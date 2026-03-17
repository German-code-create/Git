class BankAccount:
    def __init__(self, owner=None, deposit=0):
        self.owner = owner
        self.deposit = deposit

    def summa(self):
        while True:
            try:
                amount = int(input("На сколько пополнять баланс? "))
                if amount <= 0:
                    print("Ошибка. Вы ввели отрицательное число")
                    print("Попробуйте еще раз")
                else:
                    self.deposit = self.deposit + amount
                    print(f"Баланс пополнен на {amount}. Текущий баланс: {self.deposit}")
                    break
            except ValueError:
                print("Ошибка. Введите число")

    def withdraw(self):
        while True:    
            try:
                amount = float(input("Сколько снять с баланса? "))

                if amount > self.deposit:
                    print("Ошибка. Невозможно снять больше денег, чем есть на счете")
                    print(f"Вы хотели снять: {amount}. Текущий баланс {self.deposit}")
                elif amount <= 0:
                    print("Ошибка. Вы ввели отрицательное число")
                    print("Попробуйте еще раз")
                else:    
                    self.deposit = self.deposit - amount
                    print(f"Вы сняли с баланса: {amount}. Текущий баланс: {self.deposit}")
                    break
            except ValueError:            
                print("Ошибка. Введите число")
            
    def show_balance(self):
        print("Текущий баланс: ", self.deposit)
print("Как дела")
print("Я могу что то делать")