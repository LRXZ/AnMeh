from tkinter import *
from Visual import *
import json


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("GUI")
        self.window.geometry('650x350')
        lbl = Label(self.window, text="крен", font=("Times New Roman", 30))
        lbl1 = Label(self.window, text="тангаж", font=("Times New Roman", 30))
        lbl2 = Label(self.window, text="рысканье", font=("Times New Roman", 30))
        lbl3 = Label(self.window, text="угол в градусах [0;360]", font=("Times New Roman", 30))
        lbl.grid(column=0, row=1)
        lbl1.grid(column=0, row=2)
        lbl2.grid(column=0, row=3)
        lbl3.grid(column=1, row=0)
        self.scale_x = Scale(self.window, orient=HORIZONTAL, length=400, from_=0, to=360, tickinterval=45,
                             resolution=0.1)
        self.scale_y = Scale(self.window, orient=HORIZONTAL, length=400, from_=0, to=360, tickinterval=45,
                             resolution=0.1)
        self.scale_z = Scale(self.window, orient=HORIZONTAL, length=400, from_=0, to=360, tickinterval=45,
                             resolution=0.1)
        self.scale_x.grid(column=1, row=1)
        self.scale_y.grid(column=1, row=2)
        self.scale_z.grid(column=1, row=3)
        self.button_ok = Button(self.window, text='ok', width=5, height=1, bg='white', fg='black', font='arial 30',
                                command=self.click_handler)
        self.button_ok.grid(column=1, row=4)
        with open("Data.json", "r") as file:
            a0 = json.load(file)
        self.a = [(a0[0] + self.scale_x.get()) % 360, (a0[1] + self.scale_y.get()) % 360, (a0[2] + self.scale_z.get()) % 360]
        self.Matrix = Change_matrix.change_matrix(self.a[0], self.a[1], self.a[2])

    def visual(self):
        self.window.mainloop()

    def click_handler(self):
        with open("Data.json", "r") as file:
            a0 = json.load(file)
        a = [(a0[0] + self.scale_x.get()) % 360, (a0[1] + self.scale_y.get()) % 360, (a0[2] + self.scale_z.get()) % 360]
        visual(a, self.Matrix)
        with open("Data.json", "w") as write:
            json.dump(a, write)
        self.scale_x.set(0)
        self.scale_y.set(0)
        self.scale_z.set(0)
        self.Matrix = Change_matrix.change_matrix(a[0], a[1], a[2])
