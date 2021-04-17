class Car:
    total_number = 0
    def __init__(self, objfirm, objmodel, objcolor):
        self.firm = objfirm
        self.model = objmodel
        self.color = objcolor
        self.wheels = 4
        Car.total_number +=1


    def beep(self):
        print('Beep-beep!')

    def paint(self, new_color):
        self.color = new_color
        print('Теперь цвет машины:', self.color)


print(Car.total_number)
my_car = Car('Tesla', 'Roadser', 'red')
my_car2 = Car('Volswagen', 'Polo', 'white')
final_car = Car('BMW', 'M3', 'gray')
print('Производитель', my_car.firm, my_car2.firm)
print('Модель', my_car.model)
print('цвет', my_car.color)
print('Колеса', my_car.wheels)
print('Проивдитель', final_car.firm, 'Марка', final_car.model, 'color', final_car.color)
print(Car.total_number)
my_car2.beep()
my_car.paint(new_color=str(input("Введи новый цыет машины: ")))
