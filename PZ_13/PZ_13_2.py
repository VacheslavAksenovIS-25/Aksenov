# В матрице отрицательные элементы возвести в квадрат.
def square(matrix):
        square_matrix = [[x ** 2 if x < 0 else x for x in row] for row in matrix]
        print(square_matrix)

matrix = [
    [1, -2, 3],
    [3, -6, 7],
    [55, 6, -4]
]
result = square(matrix)