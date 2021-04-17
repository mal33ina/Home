print("""1. Телефон
2. Коммунальные платежи
3. Интернет
4. Свет
5. Газ""")
def oplata():
    cash = input("Введите номер карточки (16 символов): ")
    if cash.isdigit():
        if len(cash) == 16:
            print("Оплата прошла успешна")
    else:
        oplata()

def phone():
    a1 = int(input("Введите номер телефона c кодом (9 цифр): "))
    if a1 == 9:
        print("Оплата 11,70 руб.")
    else:
        phone()

def Komunall():
    a1 = input("Введите лицевой счет (7 цифр): ")
    if a1.isdigit():
        if len(a1) == 7:
            print("Оплата 74 руб.")
    else:
        Komunall()

def inet():
    a1 = input("Введите номер договора (6 цифр): ")
    if a1.isdigit():
        if len(a1) == 6:
            print("Оплата 23,45 руб.")
    else:
        inet()

def svet():
    a1 = input("Введите лицевой счет (6 цифр): ")
    if a1.isdigit():
        if len(a1) == 6:
            a3 = int(input("Введите количество киловатт: "))
            a4 = float(0.20)
            a5 = a3 * a4
            print("Оплата", "% .2f " % a5, "руб")
    else:
        svet()


def gas():
    a1 = input("Введите лицевой счет (6 цифр): ")
    if a1.isdigit():
        if len(a1) == 6:
            a3 = int(input("Введите количество кубометров газа: "))
            a4 = float(0.5082)
            a5 = a3 * a4
            print("Оплата", "% .2f " % a5, "руб")
    else:
        gas()

b = int(input("Введите номер платежа: "))
if b == 1:
    print("Заполните данные: ")
    phone()
    oplata()
elif b == 2:
    print("Заполните данные: ")
    Komunall()
    oplata()
elif b == 3:
    print("Заполните данные: ")
    inet()
    oplata()
elif b == 4:
    print("Заполните данные: ")
    svet()
    oplata()
elif b == 5:
    print("Заполните данные: ")
    gas()
    oplata()

else:
    print("Ввод не верный")