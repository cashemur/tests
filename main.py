import math


class Triangle:
    s = float()
    p = float()
    type_of_triangle = str()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def count_S(self, a, b, c):
        self.s = (((a + b + c) / 2) * (((a + b + c) / 2) - a) * (
                ((a + b + c) / 2) - b) * (
                          ((a + b + c) / 2) - c)) ** 0.5
        return self.s

    def count_P(self, a, b, c):
        self.p = a + b + c
        return self.p

    def comming_out(self, a, b, c):
        if a == c == b:
            self.type_of_triangle = "Равносторонний"
        elif a == b != c or a == c != b or c == b != a:
            self.type_of_triangle = "Равнобедренный"
        elif c ** 2 + b ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2 or a ** 2 + b ** 2 == c ** 2:
            self.type_of_triangle = "Прямоугольный"
        else:
            self.type_of_triangle = "Произвольный"
        return self.type_of_triangle

    def triangle_exist(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            print("Triangle is exist")
        else:
            print("Triangle is not exist")
            exit()
triangle = Triangle(int(input()), int(input()), int(input()))
triangle.triangle_exist(triangle.a, triangle.b, triangle.c)
triangle.count_P(triangle.a, triangle.b, triangle.c)
triangle.count_S(triangle.a, triangle.b, triangle.c)
triangle.comming_out(triangle.a, triangle.b, triangle.c)
print("S =", triangle.s, "Type =", triangle.type_of_triangle, "P =", triangle.p)
