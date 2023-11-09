from dataclasses import dataclass

class AirCastle:

    def __init__(self, high, clouds, color):
        self.high = high
        self.clouds = clouds
        self.color = color

@dataclass
class AirData:
    high: int
    clouds: int
    color: str

    def change_height(self, value):
        c = self.clouds + value
        if c < 0:
            c = 0
        self.clouds = c

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError('error')
        self.clouds += other
        self.high += other // 5
        return AirData(self.high, self.clouds, self.color)

    def opacity(self, degree):
        self.degree = self.high // degree * self.clouds
        print(f'Прозрачность облаков: {self.degree}')

    def __str__(self):
        return f'Этот воздушный замок высотой {self.high} метров, {self.color} цвета, и c {self.clouds} облаками.'

    def __eq__(self, other):
        if not isinstance(other, AirData):
            raise TypeError
        return self.clouds == other.clouds

    def __lt__(self, other):
        if not isinstance(other, AirData):
            raise TypeError
        return self.clouds < other.clouds

    def __len__(self, other):
        if not isinstance(other, AirData):
            raise TypeError
        return self.clouds <= other.clouds

castle1 = AirData(1, 3, 'Red')
castle2 = AirData(1, 5, 'Red')
print(castle1)
castle1.change_height(-10)
print(castle1)
castle1 = castle1 + 100
print(castle1)
castle1.opacity(5)
print(castle1)
print(castle2)