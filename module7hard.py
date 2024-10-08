import math


class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled = False):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
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
            self.__color = [r, g, b]
        else:
            print('Неккоректные значения РГБ')
        return self.__color

    def __is_valid_sides(self, *side):
        if all(side) > 0 and isinstance(side, int):
            # len(side) == self.sides_count  - идея измерить длину кортежа, состоящего из одного элемента провалилась
            return True
        elif all(side) > 0 and len(side) == self.sides_count:
            # в данном случае если side - кортеж
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        P = 0
        for i in self.__sides:
            P += i
        return P

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(self, *new_sides):
            self.__sides = list(new_sides)
        else:
            print('нельзя изменить количество сторон')
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __sides, __color, filled = False):
        Figure.__init__(self, __sides, __color, filled)
        self.__radius = sum(self.get_sides()) / (2 * math.pi)

    def get_square(self):
        S_circle = math.pi * (self.__radius ** 2)
        return S_circle

class Triangle(Figure):
    sides_count = 3
    def __init__(self, __sides, __color, filled = False):
        Figure.__init__(self, __sides, __color, filled)

    def get_square(self):
        p = 0.5 * (self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2])
        S_triangle = (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5
        return S_triangle



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())

circle1.set_sides(15) # Изменится
print(circle1.get_sides())