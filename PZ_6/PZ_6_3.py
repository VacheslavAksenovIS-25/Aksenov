# Дан список А размера N и целые числа К и L (1 < K < L < N). Переставить в
# обратном порядке элементы списка, расположенные между элементами Ak и Аl,
# не включая эти элементы.
import random
i = 0
A = []
try:
    N = int(input("Введите размер списка: "))
    if N > 0:
        while i < N:
            A.append(random.randint(0,100))
            i += 1
        print('Список:',A)
    else:print()
    K = int(input('Введите K: '))
    L = int(input('Введите L: '))
    if 1 < K < L < N:
        sublist = A[K+1:L]  # подсписок между индексами K и L
        reversed_sublist = reversed(sublist)  # перевернутый подсписок
        A[K+1:L] = reversed_sublist
        print("Измененный список: ",A)
    else: print('Данные введены неверно(1 < K < L < N)')
except ValueError:
    print("Неправильный тип данных")