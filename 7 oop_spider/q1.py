class Car:

    odometer = 0

    def __init__(self, make, price) -> None:
        self.make = make
        self.price = price
        self.odomater = 0

    def __str__(self) -> str:
        return "{},{},{}".format(self.make, self.price, self.odometer)

    def update_odometer(self, odometer):
        self.odometer += odometer


class ElectricCar(Car):
    def __init__(self, make, price, battary_size) -> None:
        super(ElectricCar, self).__init__(make, price)
        self.battray_size = battary_size

    def __str__(self) -> str:
        return super().__str__() + ",{}".format(self.battray_size)


def main():
    mycar = Car('Benz', 200)
    print(mycar)
    ecar = ElectricCar("telsa", 300, 80)
    ecar.update_odometer(100)
    print(ecar)


if __name__ == '__main__':
    main()