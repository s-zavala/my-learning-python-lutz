#!python
import importlib

def tester(listerclass, sept=False):

    class Super:
        def __init__(self) -> None:
            self.data1 = "Super spam"
        def ham(self):
            pass
    
    class Sub(Super, listerclass):
        def __init__(self) -> None:
            Super.__init__(self)
            self.data2 = "Sub eggs"
            self.data3 = 42
        def spam(self):
            pass
    
    instance = Sub()
    print(instance)
    if sept: print('-' * 80)

def testByNames(modname, classname, sept=False):
    modobject = importlib.import_module(modname)
    listerclass = getattr(modobject, classname)
    tester(listerclass, sept)

if __name__ == "__main__":
    testByNames('listinstance', 'ListInstance', True)
    testByNames('listinherited', 'ListInherited', True)
    testByNames('listtree', 'ListTree', False)
