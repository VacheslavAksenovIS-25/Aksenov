# Дан список размера N. Найти номера тех элементов, которые больше своего правого
# соседа, а также количество таких элементов. Найденные номера выводить в порядке
# их возрастания.
import random
list = []
result = []
i = 0
try:
    N = int(input("Введите размер списка: "))
    if N > 0:
        while i < N:
            list.append(random.randint(0,100))
            i += 1
        for i in range(len(list) - 1):
             if list[i] > list[i + 1]:
                 result.append(i)
        print("Список: ",list)
        print("Индексы элементов, которые больше своего правого соседа: ",result )
        print("Количество элементов:", len(result))
    else: print('Необходимо ввести положительное число')
except ValueError :
    print("Неправильный тип данных")

