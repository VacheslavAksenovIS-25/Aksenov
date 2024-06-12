# Задача(ПЗ №2): Скорость первого автомобиля V1 км/ч, а второго - V2 км/ч, расстояние между ними S км.
# Определить расстояние между автомобилями через Т часов, если они движутся навстречу друг другу.

from tkinter import *
from tkinter import ttk
def calculate():
    try:
        V1 = int(entry_V1.get())
        V2 = int(entry_V2.get())
        S = int(entry_S.get())
        T = int(entry_T.get())
    except:
        result_label.config(text='Ошибка: Числа не введены')

        return

    S1 = (V1 + V2) * T
    S2 = abs(S - S1)

    result_label.config(
        text=f'Расстояние между автомобилями равно:  {int(S2)} км'
    )

root = Tk()
root.title('Задача из ПЗ №2')

label = ttk.Label(root, text=' Скорость первого автомобиля V1 км/ч, а второго - V2 км/ч, расстояние между ними S км.\n'
                                 ' Определить расстояние между автомобилями через Т часов, если они движутся навстречу друг другу.',padding=5)

label.grid(column = 0, columnspan= 2, row = 0)

label_V1 = ttk.Label(root, text='Скорость первого автомобиля',padding=5)
label_V1.grid(column = 0, row = 1)
entry_V1 = ttk.Entry(root)
entry_V1.grid(column = 1, row = 1)

label_V2 = ttk.Label(root, text='Скорость второго автомобиля',padding=5)
label_V2.grid(column = 0, row = 2)
entry_V2 = ttk.Entry(root)
entry_V2.grid(column = 1, row = 2)

label_S = ttk.Label(root, text='Расстояние между автомобилями',padding=5)
label_S.grid(column = 0, row = 3)
entry_S = ttk.Entry(root)
entry_S.grid(column = 1, row = 3)

label_T = ttk.Label(root, text='Время',padding=5)
label_T.grid(column = 0, row = 4)
entry_T = ttk.Entry(root)
entry_T.grid(column = 1, row = 4)

button = ttk.Button(root, text='Рассчитать расстояние', command= calculate)
button.grid(column = 0, columnspan = 2, row = 5)

result_label = ttk.Label(root,padding=5)
result_label.grid(column = 0, columnspan = 2, row = 7)

root.mainloop()





