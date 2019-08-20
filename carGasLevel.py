"""Create a Car class that has the following characteristics:

1. It has a gas_level attribute. 2. It has a constructor (__init__ method) that takes a float representing the
initial gas level and sets the gas level of the car to this value. 3. It has an add_gas method that takes a single
float value and adds this amount to the current value of the gas_level attribute. 4. It has a fill_up method that
sets the car’s gas level up to 13.0 by adding the amount of gas necessary to reach this level. It will return a float
of the amount of gas that had to be added to the car to get the gas level up to 13.0. However, if the car’s gas level
was greater than or equal to 13.0 to begin with, then it doesnt’t need to add anything and it simply returns a 0. """


class Car:
    def __init__(self, gas_level: float):
        self.gas_level = gas_level

    def add_gas(self, amount):
        self.gas_level += amount
        return self.gas_level

    def fill_up(self):

        if self.gas_level >= 13.0:
            return 0
        else:
            amount_of_gas_necessary = 13.0 - self.gas_level
            return amount_of_gas_necessary


example_car = Car(9)
print(example_car.fill_up())
