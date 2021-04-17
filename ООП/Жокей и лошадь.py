class Horse:
    total_number = 0
    def __init__(self, obghoovs, obgcolor, obgbreed, obgname, jockei):
        self.hoovs = obghoovs
        self.color = obgcolor
        self.breed = obgbreed
        self.name = obgname
        self.jockey = jockei
        Horse.total_number += 1

    def hop(self):
        print('скачет')

    def nicker(self):
        print('игоко')

    def eat(self):
        print('ням, ням')


Loshad1 = Horse(4, 'Коричневый', 'Персидский', 'Орлик', 'Nick')
Loshad2 = Horse(4, 'red', 'Арабский', 'Каштан', 'Nick')


class Jockey:
    def __init__(self, obgname, obghorse):
        self.name = obgname
        self.horse = obghorse


Jockei = Jockey('Nick', 'Каштан')



print(Horse.total_number)
print('Количество копыт:', Loshad1.hoovs)
print('color horse:', Loshad2.color, 'Paroda:', Loshad2.breed, 'Klichka:', Loshad2.name)
print(Horse.total_number)
print('Name jokei:', Jockei.name)



