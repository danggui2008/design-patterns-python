# -*- coding: utf-8 -*- 
"""
 原型模式
"""

from abc import ABC,abstractmethod
from copy import copy,deepcopy

class Shape(ABC):
    def __init__(self,type) -> None:
       self.type = type

    @abstractmethod
    def clone(self):
        pass

class ConcretePrototypeA(Shape):
    def clone(self):
        return copy(self)
    
class ConcretePrototypeB(Shape):
    def clone(self):
        return copy(self)
    
class ConcretePrototypeC(Shape):
    def clone(self):
        return deepcopy(self)
    

if __name__ == '__main__':
    oa1 = ConcretePrototypeA('a')
    oa2 = oa1.clone()
    print(oa1.type==oa2.type)

    ob1 = ConcretePrototypeB('b')
    ob2 = ob1.clone()
    print(ob1.type==ob2.type)

    oc1 = ConcretePrototypeB('c')
    oc2 = oc1.clone()
    print(oc1.type==oc2.type)