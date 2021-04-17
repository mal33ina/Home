print("""1. Сделать заказ
2. Выйти""")
print(" Майнер здесь")
print("")
print(' У нас имеются самые востребованные на сегодняшний день "машины"! ')
print("")
a="s9" 
b="Antminer T17e - 53TH/s"
c="AvalonMiner 1066 - 50TH/s"
a2=int("1")#s9
b2=int("2")#T17
c2=int("3")#AvalonMiner
a1=int("870")
b1=int("3500")
c1=int("4500")
print("1.s9")
print("2.Antminer T17e - 53TH/s")
print("3.AvalonMiner 1066 - 50TH/s")
i=int(input("Выберите майнер: ")) 
if i==a2:
	kol=int(input("введите количество: "))
	for pods in "kol":
		print(a1*kol, "руб")
		print("Спасибо ,что выбрали нас!")
		break
elif i==b2:
	kol=int(input("введите количество: "))
	for pods in "kol":
		print(b1*kol, "руб")
		print("Спасибо ,что выбрали нас!")
		break	
elif i==c2:
	kol=int(input("введите количество: "))
	for pods in "kol":
		print(c1*kol, "руб")
		print("Спасибо ,что выбрали нас!")
		break		
else:
	print("Попробуйте еще раз ввести цифру под ,которой стоит майнер")
	