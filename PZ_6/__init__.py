# 1 задание
odd_numbers = [2*i + 1 for i in range(10)]
print(odd_numbers)

# 2 задание
def ex2(index):
    result = []
    for i in range(len(index)-1):
       if index[i] > index[i+1]:
            result.append(i)
    return result

import random
a = []
i = 0
try:
    N = int(input("Введите размер массива: "))
    while i < N:
        a.append(random.randint(0,100))
        i += 1
    print("Список: ",a)

    indices = ex2(a)
    print("Номера элементов, которые больше своего правого соседа:", indices)
    print("Количество таких элементов:", len(indices))

except ValueError:
    print("Неправильный тип данных")

# 3 задание
