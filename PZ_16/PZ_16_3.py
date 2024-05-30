# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса(3 шт.) в файл и загружать ее обратно
# Использовать модуль pickle для сериализации и десериализации обьектов Python
# в бинарном режиме.
import pickle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_square(self):
        return f'Площадь круга равна: {3.14 * self.radius ** 2}'

    def circle_length(self):
        return f'Длина круга равна: {3.14 * (2 * self.radius)}'

    def circle_diameter(self):
        return f'Диаметр круга равен: {2 * self.radius}'


def save_def():
    file = open('out.bin', 'wb')
    pickle.dump(circle1, file)
    pickle.dump(circle2, file)
    pickle.dump(circle3, file)
    file.close()


def load_def():
    file = open('out.bin', 'rb')
    first = pickle.load(file)
    second = pickle.load(file)
    third = pickle.load(file)
    print('\nИнформация,загруженная из бинарного файла',first,second,third,sep='\n')


circle1 = Circle(3)
circle2 = Circle(2)
circle3 = Circle(4)

print(circle1.circle_square())
print(circle2.circle_length())
print(circle3.circle_diameter())

save_def()
load_def()
