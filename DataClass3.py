from dataclasses import dataclass, make_dataclass, field

class Car:

    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed

@dataclass
class CarData:
    model: str
    max_speed: int
    price: int

    def get_max_speed(self):
        return self.max_speed

CarDataNew = make_dataclass('CarDataNew', [('model', str), 'max_speed', ('price', float, field(default=0))],
                            namespace={'get_max_speed': lambda self: self.max_speed})
c = Car('BMW', 160, 1000000)
print(c.__dict__)
cd = CarData('ГАЗ-322132', 999, 500000)
print(cd)
cdn = CarDataNew('Vests', 120, 4000000)
print(cdn)
print(c.get_max_speed())