from random import randint
def vvod():
	edinica = int(input(""))
	while edinica != 1:
		edinica = int(input("Введите '1': "))
	if edinica == 1:
		igra()


def igra():
	count = 0
	diapazon_ot = int(input(" Введи диапазон 'от' "))
	diapazon_do = int(input(" Введи диапазон 'до' "))
	password = randint(diapazon_ot, diapazon_do)
	vvod = int(input("Отгадай число : "))
	while vvod != password:
		vvod = int(input("Повторите попытку: "))
		count += 1
		if vvod == password:
			if count <= 3:
				print("""
				                 Ты не реально везучий ))!!!
				                 """)
			elif count > 3 and count < 6:
				print("""     
				            Счастливый человек!)
				            """)
			elif count >= 6 and count < 9:
				print(""" 
				                  Отлично!) Если это диапазон составил больше 20!)
				                  А так только - ты справился)
				                  """)
			elif count >= 10 and count < 14:
				print("""     
				             Не это не прикол, тебе сегодня не прет)))
				            """)
			elif count >= 14:
				print("""  
				                Тебе вообще не прет))))))))
				                """)
	print("Количество попыток составило: ", count)
	print("Загаданное число компьютером:", password)


print(" Угадай число, которое загадал компьютер. Проверишь на сколько ты экстрасенс) и везучий человек!\n"
"Суть игры: нужно для начала ввести диапазон чисел 'от' и 'до', а после угадать то число,\n"
"которое загадал компьютер. От количества ваших попыток будет зависеть 'текст' в конце, после вашей удачной попытке!\n"
	  "Если вы готовы, то начнаем) жми '1'")
vvod()















