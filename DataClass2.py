from dataclasses import dataclass, field
from typing import Any

@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any
    weight: Any

    def __post_init__(self):
        print('dfdfdfdffd')
        Goods.current_uid += 1
        self.uid = Goods.current_uid

@dataclass
class Book(Goods):
    title: str
    author: str
    price: float
    weight: int

    def __post_init__(self):
        super().__post_init__()
        print('dfdfdfdffd')


g = Goods(21, 44)
print(g)
# g2 = Goods( 14, 21)
# print(g2)
b = Book( 7, 5, 'fdfdfdfdfdf', 'sdssdsdsdsd')
print(b)