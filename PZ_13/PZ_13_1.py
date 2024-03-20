# Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
# последних строках и столбцах матрицы Matr2 произвольного размера
import random
def matr1():
    matr2 = [[random.randint(-100, 100) for i in range(4)] for j in range(4)]
    matr1 = [[matr2[i][j] for j in range(1, len(matr2[i])-1)] for i in range(1, len(matr2)-1)]
    print( f'Сгенерированная матрица: {matr2}')
    print(f'Новая матрица: {matr1}')
matr1()

