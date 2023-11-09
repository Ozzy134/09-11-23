from dataclasses import dataclass

@dataclass
class GoodIfrit:
    high: int
    name: str
    happy: int

    def change_goodness(self, mood):
        x = self.happy + mood
        if x < 0:
            x = 0
        self.happy = x

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError
        return GoodIfrit(self.high + other, self.name, self.happy)

    def argument(self, param):
        return f'{param * self.happy // self.high}'

    def __str__(self):
        return f'Хороший ифрит: {self.name}, высотой: {self.high}, и добрый на: {self.happy} %'

    def __eq__(self, other):
        if not isinstance(other, GoodIfrit):
            raise Exception
        return (self.happy, self.name, self.high) == (other.happy, other.name, other.high)

    def __gt__(self, other):
        if not isinstance(other, GoodIfrit):
            raise Exception
        return (self.happy, self.name, self.high) > (other.happy, other.name, other.high)

    def __ge__(self, other):
        if not isinstance(other, GoodIfrit):
            raise Exception
        return (self.happy, self.name, self.high) >= (other.happy, other.name, other.high)

    def __le__(self, other):
        if not isinstance(other, GoodIfrit):
            raise Exception
        return (self.happy, self.name, self.high) <= (other.happy, other.name, other.high)

    def __lt__(self, other):
        if not isinstance(other, GoodIfrit):
            raise Exception
        return (self.happy, self.name, self.high) < (other.happy, other.name, other.high)

    def __ne__(self, other):
        if not isinstance(other, GoodIfrit):
            raise Exception
        return (self.happy, self.name, self.high) != (other.happy, other.name, other.high)

y = GoodIfrit(20, 'Vasya', 10)
g = GoodIfrit(20, 'Anton', 15)
y.change_goodness(50)
print(y)
print(y.__add__(5))
print(y.argument(100))
print(y.high >= g.high)
print(y.high <= g.high)