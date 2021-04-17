from tkinter import *

root = Tk()


class RedButton:
    def __init__(self):
        self.b = Button(text='RED', width=10, height=5)
        self.b.bind('<Button-1>', self.change)
        self.b.pack()

    def change(self, event):
        self.b['fg'] = "red"
        self.b['activeforeground'] = "red"


RedButton()
root.mainloop()