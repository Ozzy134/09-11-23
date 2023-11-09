from dataclasses import dataclass, field, InitVar

class Vector:

    def __init__(self, x, y, z, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x ** 2 + y ** 2 + z ** 2) ** 0.5 if calc_len else 0

@dataclass(init=False)
class VectorData:
    x: int = field()
    y: int = field(compare=False)
    z: int = field(default=12)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)
    pi: float = field(init=False)


    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        self.pi = 3.14

# v = Vector(1,2,3, False)
# print(v.__dict__)
# vd = VectorData(1, 2, 3)
# vd2 = VectorData(1, 2, 3)
# print(vd, vd2)
# print(vd == vd2)

vd = VectorData(1, 2, calc_len=False)
print(vd)
