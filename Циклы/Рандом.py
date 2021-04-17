from random import randint

n = int(input("Введите количество случ:"))
for i in range(n):
    i = randint(1, 100)
    print(i, end=" ")