class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


    def new_time(self):
        self.hour = input("Введите количество часов:  ")
        self.minute = input("Введите количество минут:  ")
        self.second = input("Введите секунды:  ")
        if not self.hour.isdigit():
            self.hour = input("Введите количество часов:  ")
        if not self.minute.isdigit():
            self.minute = input("Введите количество минут:  ")
        if not self.second.isdigit():
            self.second = input("Введите секунды:  ")
        h = int(self.hour)
        m = int(self.minute)
        d = int(self.second)
        ostatok_h = h % 24
        ostatok_m = m % 60
        ostatok_s = d % 60
        chas = ostatok_h + (m // 60)
        if chas > 12:
            chas -= 12
            return (f'{h // 24} Суток,  {chas} часов (pm),'
                    f' {ostatok_m + (d // 60)} минут, {ostatok_s} секунд')
        else:
            return (f'{h // 24} Суток,  {chas} часов (am),'
                    f' {ostatok_m + (d // 60)} минут, {ostatok_s} секунд')


    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"



time = Time(16, 13, 13)

print(time.new_time())

