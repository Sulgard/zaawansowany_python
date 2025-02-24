class Figure:

    def __init__(self):
        raise NotImplementedError("Należy zaimplementować tę metodę")
    def get_field(self):
        raise NotImplementedError("Należy zaimplementować tę metodę")

    def get_circumference(self):
        raise NotImplementedError("Nalezy zaimplementowac te metode")

    def __gt__(self, other):
        return self.get_field() > other.get_field()

    def __lt__(self, other):
        return self.get_field() < other.get_field()


class Square(Figure):
    def __init__(self, side=1):
        self.side = side
        self.field = self.side ** 2

    def get_field(self):
        return self.field

    def __iadd__(self, other):
        import math
        if isinstance(other, type(int)):
            new_side = math.sqrt(self.side ** 2 + other.side ** 2)
            return type(self)(new_side)
        elif type(other) == int:
            new_side = math.sqrt(self.side ** 2 + other ** 2)
            return type(self)(new_side)
        else:
            raise TypeError(
                "unsupported operand for +: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )

    def __radd__(self, other: int):
        import math
        if type(other) == int:
            new_side = math.sqrt(self.side ** 2 + other ** 2)
            return type(self)(new_side)
        else:
            raise TypeError(
                "unsupported operand for +: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )

    def __str__(self) -> str:
        return f"Square({self.side})"

    def __add__(this, other):
        import math
        if isinstance(other, type(this)):
            new_side = math.sqrt(this.side ** 2 + other.side ** 2)
            return type(this)(new_side)
        elif type(other) == int:
            new_side = math.sqrt(this.side ** 2 + other.side ** 2)
            return type(int)(new_side)

        else:
            raise TypeError(
                "unsupported operand for +: "
                f"'{type(this).__name__}' and '{type(other).__name__}'"
            )

    def __mul__(self, scale: int | float):
        return Square(self.side * scale)

    def __truediv__(self, scale: int | float):
        return Square(self.side / scale)

    def __eq__(self, other):
        if isinstance(other, Square):
            # lub
            # if isinstance(other, type(self)):
            return self.side == other.side
        return False

    def get_circumference(self):
        return 4 * self.side


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    def get_field(self):
        import math
        return math.pi * (self.radius / 2) ** 2

    def get_circumference(self):
        import math
        return 2 * math.pi * (self.radius / 2)

if __name__ == "__main__":
    square = Square(2)
    square2 = Square(2.5)
    square3 = Square(3)
#    square.__radd__(2.5) incorrect
    print(square.__radd__(2)) # dziala
    print(square2.__add__(square))
    print(square.side)
    print(square2.side)
    print(square3.__iadd__(4))

    print("KOLO")
    circle = Circle(6)
    print(circle.radius)
    print(circle.get_field())
    print(circle.get_circumference())

    print(square.__gt__(square3))
    print(square.__lt__(square3))