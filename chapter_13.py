# 3
class Shape:
    def what_am_i(self):
        print("I'm shape")


# 1
class Rectangle(Shape):
    def __init__(self, l, w):
        self.len = l
        self.width = w

    def calculate_perimeter(self):
        return 2 * (self.len + self.width)


class Square(Shape):
    def __init__(self, x):
        self.x = x

    def calculate_perimeter(self):
        return 4 * self.x

    # 2
    def change_size(self, dx):
        self.x += dx


# 4
class Horse:
    def __init__(self, owner):
        self.owner = owner


class Rider:
    def __init__(self, name):
        self.name = name



if __name__ == '__main__':
    # 1
    rec = Rectangle(5, 4)
    sq = Square(7)
    print(f'Perimeter of rectangle: {rec.calculate_perimeter():.2f}\n' \
          f'Perimeter of square: {sq.calculate_perimeter():.2f}')

    # 3
    rec.what_am_i()
    sq.what_am_i()

    # 4
    rider = Rider('Petya')
    horse = Horse(rider)
    print(horse.owner.name)