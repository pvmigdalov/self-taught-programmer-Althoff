from math import pi

# №1
class Apple:
    def __init__(self, t, c, s, p):
        self.type = t
        self.color = c
        self.size = s
        self.price = p


# №2
class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return pi * self.radius**2


# №3
class Traingle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        p = self.a + self.b + self.c
        return p

    def area(self):
        semi_p = self.perimeter() / 2
        s = (semi_p * (semi_p - self.a) * (semi_p - self.b) * (semi_p - self.c))**0.5
        return s


# №4
class Hexagon:
    def __init__(self, sides):
        self.sides = sides

    def calculate_perimeter(self):
        return sum(self.sides)


if __name__ == '__main__':
    circle = Circle(5)
    print(f'Area of circle: {circle.area():.2f}')

    triangle = Traingle(5, 4, 3)
    print(f'Area of triangle: {triangle.area():.2f}')

    hex = Hexagon([5, 5, 5, 5, 5, 5])
    print(f'Perimeter of hexagon: {hex.calculate_perimeter()}')