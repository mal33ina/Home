kol_shkol = int(input("Коиличество школьников: "))
kol_iablok = int(input("Количество яблок: "))
korzina = kol_iablok % kol_shkol
print("В корзине: ", korzina, "яблок")
print("Каждому по ", kol_iablok // kol_shkol, "яблока")