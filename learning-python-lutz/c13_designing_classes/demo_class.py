#!python
from listtree import ListTree


class CanisLupus():
    def __init__(self, name) -> None:
        self.name = name
        self.avg_len = '41-63 in'
        self.avg_shoulder_height = '31-33 in'
        self.avg_weight = '88 lb'
    def eat(self):
        pass
    def play(self):
        pass

class CanisLupusFamiliaris(CanisLupus):
    def __init__(self, name) -> None:
        self.name = name
    
class AlaskanMalamute(CanisLupusFamiliaris, ListTree):
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    yarrow = AlaskanMalamute('Yarrow')
    smokey = CanisLupus('Smokey')
    print(yarrow)
