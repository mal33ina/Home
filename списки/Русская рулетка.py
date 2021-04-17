from random import randint
print("Введите цифру 1 или 2. 1 - орел. 2 - решка")

def imua():
    imia = input("Введите имена игроков через пробел: ")
    if imia != "":
        print("ok")
    else:
        print("Введите имя снова: ")
    razdel = imia.split(" ")
    razdel.sort()
    return razdel


def revol():
    spisok = []
    for i in range(1):
        i = spisok.append(i), randint(1, 6)
    return i



def baraban():
    correct = False
    while not correct:
        chislo = input("Введи число от 1-6: ")
        try:
            chislo == revol()
        except:
            print("Ты выграл")
            continue
        try:
            chislo != revol()
        except:
            print("kill")
            continue
        return baraban()







print(imua(),revol(), baraban())




