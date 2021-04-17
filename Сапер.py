from tkinter import *
import random


GRID_SIZE = 8          # Ширина и высота игрового поля
SQUARE_SIZE = 50       # Размер одной клетки на поле
MINES_NUM = 10         # Количество мин на поле

#Создаем основное окно программы. Задаем ему название окна «Сапер».


#Генерируем мины в случайных позициях. Для этого создаем множество mines со случайными координатами и значениями клеточек.
mines = set(random.sample(range(1, GRID_SIZE**2+1), MINES_NUM))

#Создаем сет для использованных клеточек (по которым уже нажимали).
clicked = set()

#Создаем функцию click, принимающую параметр event.
def click(event):
    ids = c.find_withtag(CURRENT)[0] #Определяем по какой клетке кликнули.
    if ids in mines:
        c.itemconfig(CURRENT, fill="red") #Если кликнули по клетке с миной - красим ее в красный цвет.
    elif ids not in clicked: #Иначе делаем проверку и красим в зеленый.
        clearance(ids)
        c.itemconfig(CURRENT, fill="green")
    c.update() #Обновляем наше поле.

#Создаем функцию mark_mine, принимающую параметр event.
def mark_mine(event):
    ids = c.find_withtag(CURRENT)[0] #Тоже определяем по какой клетке кликнули. Переменная тоже будет называться ids.
    if ids not in clicked: #Если мы не кликали по клетке - красим ее в желтый цвет, иначе - в серый.
        clicked.add(ids)
        x1, y1, x2, y2 = c.coords(ids)
        c.itemconfig(CURRENT, fill="yellow")
    else:
        clicked.remove(ids)
        c.itemconfig(CURRENT, fill="gray")

#Создаем функцию generate_neighbors, принимающую параметр square. Заполняем ее тело.
def generate_neighbors(square):

    if square == 1:      #Левая верхняя клетка
          data = {GRID_SIZE + 1, 2, GRID_SIZE + 2}
    elif square == GRID_SIZE ** 2:    #Правая нижняя
          data = {square - GRID_SIZE, square - 1, square - GRID_SIZE - 1}
    elif square == GRID_SIZE:     #Левая нижняя
          data = {GRID_SIZE - 1, GRID_SIZE * 2, GRID_SIZE * 2 - 1}
    elif square == GRID_SIZE ** 2 - GRID_SIZE + 1:    #Верхняя правая
          data = {square + 1, square - GRID_SIZE, square - GRID_SIZE + 1}
    elif square < GRID_SIZE:       #Клетка в левом ряду
          data = {square + 1, square - 1, square + GRID_SIZE, square + GRID_SIZE - 1, square + GRID_SIZE + 1}
    elif square > GRID_SIZE ** 2 - GRID_SIZE:  # Клетка в правом ряду
        data = {square + 1, square - 1, square - GRID_SIZE, square - GRID_SIZE - 1, square - GRID_SIZE + 1}
    elif square % GRID_SIZE == 0:  # Клетка в нижнем ряду
        data = {square + GRID_SIZE, square - GRID_SIZE, square - 1, square + GRID_SIZE - 1, square - GRID_SIZE - 1}
    elif square % GRID_SIZE == 1:  # Клетка в верхнем ряду
        data = {square + GRID_SIZE, square - GRID_SIZE, square + 1, square + GRID_SIZE + 1, square - GRID_SIZE + 1}
    else:  # Любая другая клетка
        data = {square - 1, square + 1, square - GRID_SIZE, square + GRID_SIZE, square - GRID_SIZE - 1,
                square - GRID_SIZE + 1, square + GRID_SIZE + 1, square + GRID_SIZE - 1}

    return data

#Теперь создадим функцию подсчета мин в соседних клетках. Пускай функция называется check_mines и принимает параметр neighbor.
def check_mines(neighbors):
    return len(mines.intersection(neighbors)) #Это достаточно просто сделать используя метод intersection типа данных сет. Возвращаем длину пересечения мин и соседних клеток

#Создаем функцию clearance, принимающую параметр ids. Заполняем ее тело.
def clearance(ids):
    clicked.add(ids)  # Добавляем клетку по которой кликнули в список
    ids_neigh = generate_neighbors(ids)  # Получаем список соседних клеток
    around = check_mines(ids_neigh)  # Определяем количество мин в соседних
    c.itemconfig(ids, fill="green")  # красим клетку  зеленый
    if around == 0:  # Если мин вокруг клетки нет
        neigh_list = list(ids_neigh)  # Создаем список соседних клеток
        while len(neigh_list) > 0:  # Пока в списке соседей есть клетки
            item = neigh_list.pop()  # Получаем клетку
            c.itemconfig(item, fill="green")  # Окрашиваем клетку в зеленый
            item_neigh = generate_neighbors(item)  # Получаем соседние клетки
            item_around = check_mines(item_neigh)
            # Получаем количество мин в соседних
            if item_around > 0:  # Если в соседних клетках есть мины
                if item not in clicked:  # Делаем эту проверку, чтобы писать по нескольку раз на той же клетке
                    x1, y1, x2, y2 = c.coords(item)  # Определяем координаты
                c.create_text(x1 + SQUARE_SIZE / 2, y1 + SQUARE_SIZE / 2,
                              text=str(item_around), font="Arial{}".format(int(SQUARE_SIZE / 2)), fill='yellow')

            else:  # Если мин в соседних клетках нет
                neigh_list.extend(set(item_neigh).difference(clicked))
                # Добавляем соседние клетки данной клетки в общий список
                neigh_list = list(set(neigh_list))
                # Убираем повторяющиеся элементы из общего списка
            clicked.add(item)  # Добавляем клетку в нажатые
    else:  # Если мины вокруг есть
        x1, y1, x2, y2 = c.coords(ids)  # Высчитываем координаты клетки
        c.create_text(x1 + SQUARE_SIZE / 2, y1 + SQUARE_SIZE / 2, text=str(around),
                          font="Arial {}".format(int(SQUARE_SIZE / 2)), fill='yellow')

root = Tk()
root.title("Сапер на PYTHON")

#ПРИВЯЗКА ОБРАБОТЧИКОВ СОБЫТИЙ ДЛЯ СОЗДАННЫХ ФУНКЦИЙ


#Задаем область на которой будем рисовать
c = Canvas(root, width=GRID_SIZE * SQUARE_SIZE, height=GRID_SIZE * SQUARE_SIZE)
c.bind("<Button-1>", click)
c.bind("<Button-3>", mark_mine)
c.pack()

#Теперь рисуем решетку из клеточек серого цвета на игровом поле, используя метод рисования прямоугольников
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        c.create_rectangle(i * SQUARE_SIZE, j * SQUARE_SIZE,
                           i * SQUARE_SIZE + SQUARE_SIZE,
                           j * SQUARE_SIZE + SQUARE_SIZE, fill='gray')

#Зацикливаем программу
root.mainloop()

















