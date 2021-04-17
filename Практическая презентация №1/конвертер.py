a=float(input("Сумма для конверции:"))
b=a/2.56#Dollar
c=a/3.12#Euro
f=a*33.3#Рос.руб.
d=input("Выбор валюты:")
if d=="dollar":
	print(b)
elif d=="euro":
	print(c)
elif d=="Рос.руб.":
	print(f)
else:
	print("Не верный ввод валюты")