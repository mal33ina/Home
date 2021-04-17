class Pochta:

    def __init__(self, objindex, objstreet, objnomer, objfirstname, objsurname):
        self.index = objindex
        self.street = objstreet
        self.nomer = objnomer
        self.firsname = objfirstname
        self.surname = objsurname
        try:
            self.index = int(self.index)
        except ValueError:
            print("Надо ввести цифры")



    def new_kol(self, new_index):
        self.index = new_index
        try:
            self.index != int(new_index)
        except ValueError:
            print("Надо ввести цифры")
        return 'Ваш индекс изменился на: ', self.index



    def __str__(self):
        return f'Индекс:{self.index},Улица: {self.street},Номер здания:{self.nomer}, Имя: {self.firsname}, Фамилия: {self.surname}'






adress = Pochta(220005, 'Петруся Бровки', 45, str(input("Введите имя: ")), str(input("Введите Фамилию: ")))
adress1 = Pochta(220040, "Куйбышева", 69, str(input("Введите имя: ")), str(input("Введите Фамилию: ")))

print(f'Индекс:{adress.new_kol(input())},Улица: {adress.street},Номер здания:{adress.nomer}, Имя: {adress.firsname}, Фамилия: {adress.surname}')
print(f'Индекс:{adress1.index},Улица: {adress1.street},Номер здания:{adress1.nomer}, Имя: {adress1.firsname}, Фамилия: {adress.surname}')
print(adress)
print(adress1)


