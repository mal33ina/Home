a=str(input("Кушать хочешь?: "))
if a=="Да":
    c=str(input("В меню есть: картошка, пельмени, паста."
                "Ваш выбор:  "))
    if c=="картошка":
        print("Очень долго готовить")
    elif c=="паста":
        print("Ок, сейчас подогреем")
    elif c=="пельмени":
        print("Закончилась сметана-бывает.")
else:
    print("")

