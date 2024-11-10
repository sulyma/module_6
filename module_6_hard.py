import math


class Figure:
    def __init__(self, color=(0, 0, 0), *sides):
        self.__color = color
        self.filled = False

        if len(sides) == 0 or not self.is_valid_sides(*sides):
            self.sides = [1 for _ in range(self.sides_count())]
        else:
            self.sides = list(sides)

    def sides_count(self):
        return 0

    def get_color(self):
        return self.__color

    def is_valid_color(self, r, g, b):
        return all([isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b)])

    def set_color(self, r, g, b):
        if self.is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def is_valid_sides(self, *new_sides):
        return (
                len(new_sides) == self.sides_count()
                and all(isinstance(side, int) and side > 0 for side in new_sides)
        )

    def get_sides(self):
        return self.sides

    def set_sides(self, *new_sides):
        if self.is_valid_sides(*new_sides):
            self.sides = list(new_sides)

    def __len__(self):
        return sum(self.sides)


class Circle(Figure):
    def sides_count(self):
        return 1

    def radius(self):
        circumference = self.get_sides()[0]
        return circumference / (2 * math.pi)

    def square(self):
        return math.pi * self.radius() ** 2


def heron(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


class Triangle(Figure):
    def sides_count(self):
        return 3

    def square(self):
        a, b, c = self.get_sides()
        return heron(a, b, c)


class Cube(Figure):
    def sides_count(self):
        return 12

    def __init__(self, color=(0, 0, 0), edge_length=1):
        super().__init__(color, *(edge_length for _ in range(self.sides_count())))

    def volume(self, edge_length):
        return edge_length ** 3

    def get_volume(self):
        edge_length = self.sides[0]
        return self.volume(edge_length)


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
