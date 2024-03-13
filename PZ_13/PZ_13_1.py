# Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
# последних строках и столбцах матрицы Matr2 произвольного размера
def matr1(matr2):
    matr1 = [[matr2[i][j] for j in range(1, len(matr2[i])-1)] for i in range(1, len(matr2)-1)]
    print(f'Новая матрица: {matr1}')

matr2 = [
    [2, 6, 12],
    [2, 15, 3],
    [1, 8, 3]
]
result = matr1(matr2)

