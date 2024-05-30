# Создайте класс "Фигура", который содержит метод расчета площади фигуры.
# Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса
# "Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры.
class Figure:
    def __init__(self, side, high):
        self.side = side
        self.high = high

    def figure_square(self):
        return f'{self.side * self.high}'

class Square(Figure):
    def square_square(self, side_sq):
        return f'{side_sq ** 2}'


class Rectangle(Figure):
    def rectangle_square(self, rec_length, rec_width):
        return f'{rec_length * rec_width}'

figure = Figure(3,6)
square = Square(3,4)

print(square.figure_square())
print(square.square_square(3))
print(issubclass(Square, Figure))
print(issubclass(Figure, Square))
print(square.__dict__)