def tekst():
    mal = 0
    bol = 0
    cif = 0
    for i in vvod:
        if 'a' <= i <= 'z':
            mal += 1
        elif 'A' <= i <= 'Z':
            bol += 1
        elif 'а' <= i <= 'я':
            mal += 1
        elif 'А' <= i <= 'Я':
            bol += 1
        elif '0' <= i <= '9':
            cif += 1
        else:
            pass
    print('Нижний регистр', mal, 'букв')
    print("Верхний регистр ", bol, "букв")
    print("Количество цифр:", cif)

vvod = str(input("Напишите текст: "))
tekst()


