import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b


    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not isinstance(side, int) and side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides



class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, __sides, filled=False):
        super().__init__(__color, __sides)
        self.__radius = __sides / (2 * math.pi)

    def get_square(self):
        S_circle = math.pi * (self.__radius ** 2)
        return S_circle


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides, height, filled=False):
        super().__init__(__color, __sides, filled)
        self.__height = height

    def get_square(self):
        p = 0.5 * (self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2])
        S_triangle = (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5
        return S_triangle

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side, filled=False):
        cube_sides = [side] * 12
        super().__init__(color, *cube_sides, filled=filled)


    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
