import time
import random
login = 'admin'
# Спросите у пользователя логин и сравните со своим
user_login = input('Ваш логин: ')
if user_login == login:
    print('Добро пожаловать, создатель! Что вы хотите изменить?')
if user_login != login:
    print('Добро пожаловать,', user_login, '!')
    command = input('Какую игру вы выберете дверная игра,канкулятор,время,квиз,игра 2:')
    if command == 'дверная игра':
        time.sleep(1)
        print('Добро пожаловать в игру!')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        door = input('Какую дверь вы выбирете 1/2/3:')
        if door == '1':
            print('вам дали 70 монет')
        elif door == '2':
            print("на вас упал жирный однокласник")
        elif door == '3':
            print("вам дали 33 монеты")
        coins = int(input("Сколько монет вы собрали? "))
        if coins == 70:
            print("Вы прошли 1 уровень")
        if coins == 33:
            print("Вы проиграли пройдите уровень заново")
if command == 'канкулятор':
    def add(x, y):
        return x + y


    def subtract(x, y):
        return x - y


    def multiply(x, y):
        return x * y


    def divide(x, y):
        if y == 0:
            return "Ошибка! Деление на ноль."
        else:
            return x / y


    print("Выберите операцию:")
    print("1.Сложение")
    print("2.Вычитание")
    print("3.Умножение")
    print("4.Деление")

    choice = input("Введите номер операции(1/2/3/4): ")

    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Ошибка ввода! Вы ввели недопустимый символ.")
if command == 'время':
    from datetime import datetime
    current_datetime = datetime.now()
    print(current_datetime.year, 'год')
    print(current_datetime.month, 'месяц')
    print(current_datetime.day, 'день')
    print(current_datetime.hour, 'часов')
    print(current_datetime.minute, 'минут')
    print(current_datetime.second, 'секунд')
if command == 'квиз':
    point = 0
    print("Добро пожаловать в квиз на тему Солнца!")
    print("Ответьте на следующие вопросы:")

    # Вопрос 1
    print("n1. Какой тип звезды является Солнце?")
    print("   a) Красный карлик")
    print("   b) Белый карлик")
    print("   c) Главная последовательность")
    answer = input("Ваш ответ: ").lower()
    if answer == "c":
        print("Правильно!")
        point += 1
    else:
        print("Неправильно!")

    # Вопрос 2
    print("n2. Какой диаметр у Солнца?")
    print("   a) Приблизительно 1 000 километров")
    print("   b) Приблизительно 10 000 километров")
    print("   c) Приблизительно 1 000 000 километров")
    answer = input("Ваш ответ: ").lower()
    if answer == "c":
        print("Правильно!")
        point += 1
    else:
        print("Неправильно!")

    # Вопрос 3
    print("n3. Какой процент массы в солнечной системе принадлежит Солнцу?")
    print("   a) Приблизительно 99%")
    print("   b) Приблизительно 60%")
    print("   c) Приблизительно 90%")
    answer = input("Ваш ответ: ").lower()
    if answer == "a":
        print("Правильно!")
        point += 1
    else:
        print("Неправильно!")

    # Вопрос 4
    print("n4. Какая температура на поверхности Солнца?")
    print("   a) Приблизительно 2 000 градусов Цельсия")
    print("   b) Приблизительно 15 000 градусов Цельсия")
    print("   c) Приблизительно 5 000 градусов Цельсия")
    answer = input("Ваш ответ: ").lower()
    if answer == "b":
        print("Правильно!")
        point += 1
    else:
        print("Неправильно!")

    # Вопрос 5
    print("n5. В какой глактике находится солнечная система?")
    print("   a) Галактика Андромеда")
    print("   b) Галактика Млечный Путь")
    print("   c) Это ходящия система")
    answer = input("Ваш ответ: ").lower()
    if answer == "b":
        print("Правильно!")
        point += 1
    else:
        print("Неправильно!")

    # Вывод результатов
    print("Вы завершили квиз!")
    print("Ваш итоговый счет:", point, "из 5 возможных.")
if command == 'игра 2':
    player_score = 0
    comp_score = 0
    while True:
        player = input('камень ножницы или бумага?:')
        time.sleep(0.5)
        comp = random.randint(1, 3)
        if comp == 1:
            comp = "камень"
            print('комп выбрал камень')
        elif comp == 2:
            comp = "ножницы"
            print("комп выбрал ножницы")
        elif comp == 3:
            comp = 'бумага'
            print('комп выбрал бумагу')
        if player == ("камень" and comp == "ножницы") or (player == "ножницы" and comp == "бумага") or (
                player == "бумага" and comp == "камень"):
            player_score += 1
            print('ты выйграл у тебя', player_score, 'очков')
        elif (player == "камень" and comp == "камень") or (player == "бумага" and comp == "бумага") or (
                player == "ножницы" and comp == "ножницы"):
            print('ничья')
        elif player_score == 2:
            print('ты набрал 3 очка ты победил')
            command = input('Какую игру вы выберете дверная игра,канкулятор,время,квиз,игра 2:')
        elif comp_score == 2:
            print('комп набрал 3 очка комп победил')
            command = input('Какую игру вы выберете дверная игра,канкулятор,время,квиз,игра 2:')
        else:
            comp_score += 1
            print('комп выйграл у комп', comp_score, 'очков')
while True:
    command = input('Какую игру вы выберете дверная игра,канкулятор,время,квиз,игра 2:')
