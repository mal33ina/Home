def step():     # Степень
    if znak == "^":
        print(chislo1**chislo2)
#######################################

def fact():  # Факториал
    if znak == "!":
        i = chislo1
        factorial = 1
        while i > 1:
            factorial = factorial * i
            i -= 1
        print(factorial)
############################################
def modul():       # Модуль
    if znak == "||":
        print(abs(chislo1))
###############################################
def procent():   # Процент
    if znak == "%":
        print((chislo1/100) * chislo2)
##############################################
import math
def logorif():      # Логорифм
    if znak == "log":
        print('% .4f ' % math.log(chislo1, chislo2))
#############################################
def slogen(): # сложение
    if znak == "+":
        print(chislo1+chislo2)
###########################################
def minus(): # вычетание
    if znak == "-":
        print(chislo1-chislo2)
###########################################
def umnog(): # Умноженеие
    if znak == "*":
        print(chislo1*chislo2)
#########################################
def delen(): # Деление
    if znak == "/":
        print(chislo1/chislo2)
##########################################


chislo1 = float(input("Введите число: "))
znak = input("Введите символ: ")
if znak == "!" or znak == "||":
    if znak == "!":
        fact()
    elif znak == "||":
        modul()
else:
    chislo2 = float(input("Введите 2-е число: "))
slogen()
minus()
delen()
umnog()
step()
logorif()
procent()
