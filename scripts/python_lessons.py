class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def print_cars(self):
        for car in (blue_car, red_car):
            print(f"The {car.color} car has {car.mileage:,} miles")


blue_car = Car(color="blue", mileage=20_000)
red_car = Car(color="red", mileage=30_000)

blue_car.print_cars()