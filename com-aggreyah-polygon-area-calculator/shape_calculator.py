class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** 0.5

    def get_picture(self):
        line = ("*" * self.width)
        line = f"{line}"
        height = ""
        for i in range(self.height):
            height += f"{line}\n"
        if len(line) > 50 or len(height.split("\n")) > 50:
            return "Too big for picture."
        else:
            return height

    def get_amount_inside(self, other_shape):
        my_area = self.get_area()
        other_area = other_shape.get_area()
        return int(my_area / other_area)

    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.height = side
        self.width = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"{self.__class__.__name__}(side={self.height})"


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
