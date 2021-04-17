import random  
import time

def display_intro():
	print(""" Ты- Шрек, спасающий Фиону.
	Сейчас ты находишься между 2 я башнями.
	В одной башне тебя ждет Фиона.
	А в другой - дракон, который за секунду тебя испопелит.""")
	
def choose_tower():
	tower = input(" Введите число: ")
	while tower != "1" and tower != "2":
		tower = input("выбермте 1 или 2: ")
		return int(tower)

def check_tower(chooseTower):
	print("Прибилижаетесь к башне")
	time.sleep(2)
	print("Она темная и жудкая")
	time.sleep(2)
	print("Перед тобой резко открывается дверь и из нее на тебя пристально смотрит....")
	print()
	time.sleep(2)
	rand = random.randint(1, 2)
	if rand == chooseTower:
		print("Спас Фиону")
	else:
		print("погиб")
		
shrek = "yes"				
while shrek == "yes" or shrek == "y":
	display_intro()
	nomer_tower = choose_tower()
	check_tower(nomer_tower)

	


		
		
	
