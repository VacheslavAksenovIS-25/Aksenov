V1 = int(input('Введите скорость первого автомобиля'))
V2 = int(input('Введите скорость второго автомобиля'))
S1 = int(input('Введите начальное расстояние между автомобилями'))
T = int(input('Введите время'))
S = int((V1+V2)*T)
S2 = int(abs(S - S1))
print('Расстояние между авто равняется:', S2)