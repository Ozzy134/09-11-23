from dataclasses import dataclass
from pprint import pprint

class Thing:

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f'name = {self.name}, weight = {self.weight}, price = {self.price}'

@dataclass
class ThingData:
    name: str
    weight: int
    price: float

    def __eq__(self, other):
        return self.price == other.price

t = Thing('book', 1, '2 $')
print(t)
td = ThingData('magazine', 1, 3.5)
td2 = ThingData('magazine', 1, 3.5)
print(td == td2)