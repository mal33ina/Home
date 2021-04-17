klava = (('1', 'a', 'b', 'c'), ('2', 'd', 'e', 'f'), ('3', 'g', 'h', 'i'), ('4', 'j', 'k', 'l'),
               ('5', 'm', 'n', 'o'), ('6', 'p', 'q', 'r'), ('7', 's', 't', 'u'), ('8', 'v', 'w', 'x'),
               ('9', 'y', 'z',), ('0', '.', ',', '!'), ('#', '_'))
kolichestvo = 0
text = input('Введите текст: (Для выхода из программы наберите "0") \n')
while text != '0':
    try:
        text = int(text)
    except:
        print('Числа вводить нельзя')

    if len(text) < 1000:
        price = 0
        for bukva in text:
            for kortezh in klava:
                if bukva in kortezh:
                    price += kortezh.index(bukva)
        print(price)
        kolichestvo += price
    text = input('Введите текст: \n')
print(kolichestvo)







