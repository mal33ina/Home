my_list = input("Введите список покупок: ")
my_list2 = my_list.split(",")
ikea_list = ["стол", "шкаф", "кресло", "доска"]
for begun in my_list2:
    for begun2 in ikea_list:
        if begun == begun2:
            print(begun)

