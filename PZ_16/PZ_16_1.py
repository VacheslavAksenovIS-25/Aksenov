# Создайте класс "Круг", который имеет атрибут радиуса и методы для вычисления
# площади, длины окружности и диаметра.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_square(self):
        return f'Площадь круга равна: {3.14 * self.radius ** 2}'

    def circle_length(self):
        return f'Длина круга равна: {3.14 * (2 * self.radius)}'

    def circle_diameter(self):
        return f'Диаметр круга равен: {2 * self.radius}'


circle = Circle(3)
print(circle.circle_square())
print(circle.circle_length())
print(circle.circle_diameter())
