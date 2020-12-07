from car import Car


class SolarCar(Car):
    def __init__(self, gas_tank, engine, wheels):
        super(SolarCar, self).__init__(gas_tank, engine, wheels)

    def accelerate(self):
        print('Швидкість машини на сонячних батареях ' + str(self.speed))
        super(SolarCar, self).accelerate()

    def turn(self, side):
        print('Машина на сонячних батареях повернула')
        super(SolarCar, self).turn(side)

    def brake(self):
        super(SolarCar, self).brake()
        print('Машина на сонячних батареях зупинилась')
        print('--------------------------------------')

    def get_wheels_count(self):
        super(SolarCar, self).get_wheels_count()
