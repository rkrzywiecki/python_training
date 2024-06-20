class Car:
    def __init__(self, model: str, colour: str, initial_speed: int = 0) -> None:
        self.model = model
        self.colour = colour
        if initial_speed < 5:
            self.__speed = 0
        else:
            self.__speed = initial_speed

    def speed_up(self):
        self.__speed += 5

    def slow_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5

    def show_speed(self):
        print("Current speed:", self.__speed)


my_lovely_car = Car("T=Roc", "Red", 5)
my_lovely_car.speed_up()
my_lovely_car.speed_up()
my_lovely_car.slow_down()
my_lovely_car.slow_down()
my_lovely_car.slow_down()
my_lovely_car.slow_down()
my_lovely_car.show_speed()
