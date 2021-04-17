x = str(input("Введите слово: "))
if "музыка" in x.lower():
    print("Тыц")
    print("тЫц")
    print("тыЦ")
    print("Тыц")
    print("тЫц")
    print("тыЦ")
    print("):")


musik = input('введите слово музыка')
tiz = "тыц"
if "музыка" in musik.lower():
    for num in range(len(tiz)):
        print(tiz.capitalize())
        print(tiz[0]+tiz[1].swapcase()+tiz[2])
        print(tiz[0]+tiz[1]+tiz[2].swapcase())