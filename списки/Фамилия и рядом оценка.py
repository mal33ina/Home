from random import randint
spisok_famil = []
for i in range(5):
    spisok_famil.append(input("Ведите фамилии (5): "))
spisok_chisel = []
for i in range(5):
    spisok_chisel.append(randint(1, 10))
a = list(spisok_famil)
c = list(spisok_chisel)
for i in range(5):
    print(a[i], c[i])










