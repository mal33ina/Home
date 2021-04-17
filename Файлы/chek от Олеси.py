#Все мы в магазин ходим со списком покупок.
#Так вот представь себя на месте онлайн-магазина.
#Пользователь вводит, что именно ему надо (наименование).
#Если оно имеется в файле расценок магазина ‘prices.txt’, то пользователь получает сообщение, что  товар в наличии и можно ввести необходимое количество.
#После ввода количества, пользователь должен ввести свой email.
#Пользователь получает чек на email. (Создать файл, где email пользователя будет названием файла)

spisok_names = []
spisok_prices = []
shopper = True
while shopper:
    shoper = input("Введите товар, который ищите (0 - если хотите закончить покупки)\t")
    price = open("D:\price.txt", "r", 1, "utf-8")
    if shoper == "0":
        shopper = False
    else:
        for i in price:
            ii = i.split()
            if ii[0] == shoper.lower():
                print("Товар есть в наличии")
                spisok_names.append(ii[0])
                col = int(input("Введите количество либо вес, который вам необходим\t"))
                spisok_prices.append(float(ii[1]) * col)
    price.close()
for elem in range(len(spisok_names)):
    print(f"{spisok_names[elem]}---{spisok_prices[elem]}")