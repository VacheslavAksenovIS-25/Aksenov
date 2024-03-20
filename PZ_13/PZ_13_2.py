# В матрице отрицательные элементы возвести в квадрат.
import random
def square():
        matrix = [[random.randint(-100, 100) for i in range(3)] for j in range(3)]
        square_matrix = ([x ** 2 if x < 0 else x for x in row] for row in matrix)
        print(f'Сгенерированная матрица: {matrix}')
        print(f'Измененная матрица: {list(square_matrix)}')
square()
