class Shape:
    def what_am_i(self):
        print("I'm shape")


class Square(Shape):
    square_list = [] # 1

    def __init__(self, x):
        self.x = x
        self.square_list.append(self)

    def __repr__(self): # 2
        return f'{self.x} на {self.x} на {self.x} на {self.x}'

    def calculate_perimeter(self):
        return 4 * self.x

    # 2
    def change_size(self, dx):
        self.x += dx


# 3    
def compare(obj1, obj2):
    return obj1 is obj2




if __name__ == '__main__':
    # 1
    sq1 = Square(5)
    sq2 = Square(6)
    sq3 = Square(5)

    for sq in Square.square_list:
        print(sq.x)

    # 2
    print(sq1)

    # 3
    sq4 = sq1
    print(compare(sq1, sq2))
    print(compare(sq1, sq4))
