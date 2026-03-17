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
    
    def __str__(self):  # Изменено с __repr__ на __str__
        return f"{self.owner},{self.deposit}"

accounts = []

def save(accounts, filename='C:\\prog\\acc.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for account in accounts:
            file.write(str(account) + '\n')

def register():
    while True:
        name = input("Введите имя пользователя: ")
        if name.strip() == "":  # Проверка на пустое имя
            print("Ошибка. Введите имя пользователя")
        else:
            break
    
    # Проверка существования пользователя
    for acc in accounts:    
        if acc.owner.lower() == name.lower():
            print(f"Пользователь с именем {name} уже существует!")
            return None
    
    while True:
        try:
            initial = float(input("Введите начальный баланс (0 если без денег): "))
            if initial < 0:
                print("❌ Баланс не может быть отрицательным!")
            else:
                break
        except ValueError:
            print("❌ Введите число!")
    
    new_account = BankAccount(name, initial)
    accounts.append(new_account)
    print(f"✅ Пользователь {name} успешно зарегистрирован!")
    print(f"💰 Начальный баланс: {initial} руб.\n")
    
    # Сохраняем в файл
    with open('C:\\prog\\acc.txt', 'a', encoding='utf-8') as file:
        file.write(str(new_account) + '\n')
    
    return new_account 

def find_user_balance(search_name):
    with open('C:\\prog\\acc.txt', 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            
            # Разделяем по запятой
            parts = line.split(',')
            if len(parts) >= 2:
                name = parts[0].strip()
                balance = float(parts[1].strip())
                
                if name.lower() == search_name.lower():
                    print(f"✅ Пользователь '{name}' найден")
                    return balance, line_num
    
    print(f"❌ Пользователь '{search_name}' не найден")
    return None, None  # Возвращаем два None вместо одного

def replace_line_by_number(line_number, new_text):
    with open('C:\\prog\\acc.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    if line_number < 1 or line_number > len(lines):
        print("Некорректно указана строка")
        return
    
    lines[line_number - 1] = new_text + '\n' 
    
    with open('C:\\prog\\acc.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)

# Основная программа
while True:
    print("\n1. Создать аккаунт")
    print("2. Сохранить пользователей")
    print("3. Выбрать пользователя")
    print("4. Выход")
    
    while True:
        try:
            num = int(input("Выберите действие: "))
            break
        except ValueError:
            print("Ошибка. Введите число")
    
    if num == 1:
        register()
    elif num == 2:
        save(accounts)
        print("Пользователи успешно сохранены")
    elif num == 3:
        while True:
            name = input("Введите имя пользователя: ")
            result = find_user_balance(name)
            
            if result[0] is not None:  # Проверяем, найден ли пользователь
                balance, line1 = result
                owner1 = BankAccount(name, balance)
                break
            else:
                print("Попробуйте еще раз")
        
        # Меню операций с выбранным пользователем
        while True:
            print('\n1. Положить деньги на счет')
            print('2. Снять деньги')
            print('3. Перевести деньги на другой счет')
            print('4. Показать текущий баланс')
            print('5. Выйти из системы')
            
            while True:
                try:
                    nums = int(input("Выберите действие: "))
                    break
                except ValueError:
                    print("Ошибка. Введите число")
            
            print()
            
            if nums == 1:
                owner1.summa()
                replace_line_by_number(line1, str(owner1))  # Исправлено: str(owner1)
                
            elif nums == 2:
                owner1.withdraw()
                replace_line_by_number(line1, str(owner1))  # Исправлено: str(owner1)
                
            elif nums == 3:
                name = input("Введите имя пользователя для перевода: ")
                result = find_user_balance(name)
                
                if result[0] is not None:
                    balance2, line2 = result
                    owner2 = BankAccount(name, balance2)
                    
                    try:
                        money = float(input("Введите сумму для перевода: "))
                        
                        if money <= 0:
                            print("Ошибка. Сумма должна быть положительной")
                        elif owner1.deposit >= money:
                            owner1.deposit -= money
                            owner2.deposit += money
                            print("✅ Деньги успешно переведены")
                            
                            # Обновляем файлы
                            replace_line_by_number(line1, str(owner1))
                            replace_line_by_number(line2, str(owner2))
                            
                            print("Ваш баланс: ", end="")
                            owner1.show_balance()
                        else:
                            print("❌ Недостаточно средств")
                    except ValueError:
                        print("Ошибка. Введите число")
                else:
                    print("Пользователь для перевода не найден")
                
            elif nums == 4:
                owner1.show_balance()
                
            elif nums == 5:
                print("До свидания")
                save(accounts)
                break
            else:
                print("Ошибка. Выберите из предложенных вариантов")
        break  # Выходим из цикла выбора пользователя
    
    elif num == 4:
        print("Программа завершена")
        save(accounts)
        break
    
    else:
        print("Ошибка. Выберите из предложенных вариантов")