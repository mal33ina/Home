p1= "15"
print(1, "Много всего" , p1, "кв. см", sep= ",")


a=245.543
print("%.5f"%a)
print("%.4f"% 3.1415926)
print("""1
2
3""")
a = 3; b = 5
print("F", b, " = ", a,sep= " ")
print(24, 46)
print("{:10.3f}".format(-4/3), sep="")
def ticket():   #это описание функции
	amount = input("сколько вы хотите купить билетов? ")
	price = 5
	cost = amount * price
	print(f"Общая стоимость билетов: {cost}.")

def countFood():
    a = int(input())
    b = int(input())
    print("Всего", a+b, "шт.")

print("Сколько бананов и ананасов для обезьян?")
countFood()

print("Сколько жуков и червей для ежей?")
countFood()

print("Сколько рыб и моллюсков для выдр?")
countFood()

