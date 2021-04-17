class Geomet:
    def __init__(self, objznach, objcolor):
        self.znach = objznach
        self.color = objcolor


class Tr(Geomet):
    def tr(self):
        a = self.znach * 3
        return a

class Kv(Geomet):
    def kv(self):
        a = self.znach * 4
        return a

class Kr(Geomet):
    def kr(self):
        a = self.znach * 3.14 * 2
        return a


Treugolnick = Tr(5, 'blue')
Kvadrat = Kv(4, 'red')
Krug = Kr(7, 'white')

print(f'Периметр треугольника: {Treugolnick.tr()} см, color: {Treugolnick.color}')
print(f'Периметр квадрата: {Kvadrat.kv()} см, color: {Kvadrat.color}')
print(f'Площадь круга: {Krug.kr()} см**2, color: {Krug.color}')
