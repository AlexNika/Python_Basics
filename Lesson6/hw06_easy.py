# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt
from math import acos
from math import pi


class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.xy = sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
        self.yz = sqrt((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2)
        self.zx = sqrt((z[0] - x[0]) ** 2 + (z[1] - x[1]) ** 2)
        self.sp = (self.xy + self.yz + self.zx) / 2

    def chk_triangle(self):
        _sum_xy_yz = self.xy + self.yz
        _sum_yz_zx = self.yz + self.zx
        _sum_zx_xy = self.zx + self.xy
        try:
            _alpha = 180 * acos((self.yz ** 2 + self.zx ** 2 - self.xy ** 2) / (2 * self.yz * self.zx)) / pi
            _beta = 180 * acos((self.xy ** 2 + self.zx ** 2 - self.yz ** 2) / (2 * self.xy * self.zx)) / pi
            _gamma = 180 * acos((self.xy ** 2 + self.yz ** 2 - self.zx ** 2) / (2 * self.xy * self.yz)) / pi
        except ZeroDivisionError:
            return False
        if (_alpha + _beta + _gamma) == 180 and \
                (_sum_xy_yz > self.zx and _sum_yz_zx > self.xy and _sum_zx_xy > self.yz):
            return True
        else:
            return False

    def area(self):
        return sqrt(self.sp * (self.sp - self.xy) * (self.sp - self.yz) * (self.sp - self.zx))

    def perimeter(self):
        return self.xy + self.yz + self.zx

    def height(self):
        return 2 * self.area() / self.xy


t1 = Triangle((1, 10), (100, 10), (100, -100))
if t1.chk_triangle():
    print('Треугольник с заданными координатами существует')
    print(f'Площадь треугольника t1: {t1.area():.2f}')
    print(f'Высота треугольника t1: {t1.height():.2f}')
    print(f'Периметр треугольника t1: {t1.perimeter():.2f}')
else:
    print('Треугольник с заданными координатами НЕ существует!')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.ab = sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        self.bc = sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)
        self.cd = sqrt((c[0] - d[0]) ** 2 + (c[1] - d[1]) ** 2)
        self.da = sqrt((d[0] - a[0]) ** 2 + (d[1] - a[1]) ** 2)

    def chk_trapezoid(self):
        _d1 = sqrt(self.ab ** 2 + self.bc * self.da)
        _d2 = sqrt(self.cd ** 2 + self.bc * self.da)
        if _d1 == _d2:
            return True
        else:
            return False

    def perimeter(self):
        return self.ab + self.bc + self.cd + self.da

    def area(self):
        return (self.bc + self.da) / 4 * sqrt(4 * self.ab ** 2 - (self.bc - self.da) ** 2)


t2 = Trapezoid((0, 0), (10, 10), (60, 10), (70, 0))
if t2.chk_trapezoid():
    print('Трапеция равнобочная')
    print(f'Длины сторон равнобочной трапеции t2: {t2.ab:.2f}, {t2.bc:.2f}, {t2.cd:.2f}, {t2.da:.2f}')
    print(f'Площадь трапеции t2: {t2.area():.2f}')
    print(f'Периметр трапеции t2: {t2.perimeter():.2f}')
else:
    print('Трапеция НЕ равнобочная')
