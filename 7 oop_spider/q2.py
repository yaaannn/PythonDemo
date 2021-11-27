class MyComplex:
    def __init__(self, real, imag) -> None:
        self.real = real
        self.imag = imag

    def __str__(self) -> str:
        return "({})+({})j\n".format(self.real, self.imag)

    def __add__(self, other):
        return "({})+({})i".format(self.real + other.real,
                                   self.imag + other.imag)

    def __sub__(self, other):
        return "({})+({})i".format(self.real - other.real,
                                   self.imag - other.imag)

    def __mul__(self, other):
        return "({})+({})i".format(
            self.real * other.real - self.imag * other.imag,
            other.real * self.imag + self.real * other.imag)


def main():
    c1 = MyComplex(3, -5)
    c2 = MyComplex(2, 3)
    print(c1, c2)
    print("c1+c2=", c1 + c2)
    print("c1-c2=", c1 - c2)
    print("c1*c2=", c1 * c2)


if __name__ == "__main__":
    main()