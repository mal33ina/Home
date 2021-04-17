from tkinter import*
root = Tk()
root.geometry("225x230")
root.resizable()
root.resizable(width=False, height=False)
root.title("Learning English")
menu1 = Button(root, text="...", width=300, height=7)
menu2 = Button(root, text="...", width=300, height=7)


def showMenu():
    menu1.pack()


def hideMenu():
    menu2.pack_forget()










