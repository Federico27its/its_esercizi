from Exercise1_Circle import Circle

from Exercise1_Rectangle import Rectangle


if __name__ == "__main__":
    r = Rectangle(10, 20)
    c = Circle(10)

    print(r.base(), r.height())
    print(r.perimeter(), r.area())

    print(c.radius())
    print(c.perimeter(), c.area())