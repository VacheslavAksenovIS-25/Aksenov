# вывод расстояния между автомобилями через Т часов,если они движутся навстречу
V1 = int(input('Введите скорость первого автомобиля,км/ч'))
V2 = int(input('Введите скорость второго автомобиля,км/ч'))
S = int(input('Введите начальное расстояние между автомобилями,км'))
T = int(input('Введите время'))
S1 = int((V1+V2)*T) # общий путь
S2 = int(abs(S - S1)) # модуль разности расстояний
print('Расстояние между авто через',T,'ч равняется:', S2 ,'км')