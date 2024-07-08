"""
template模式
"""

from abc import ABC,abstractmethod

#AbstractClass【抽象类（Abstract Class）】
class AbstractClass(ABC):
    #模板方法：定义骨架
    def templateMethod(self): 
        self.step1()
        self.step2()
        self.step3()
        self.step4()
    
    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass

    @abstractmethod
    def step4(self):
        pass

class ConcreteClass(AbstractClass):
    def step1(self):
        print('ConcreteClass step1')
    
    def step2(self):
        print('ConcreteClass step2')
    
    def step3(self):
        print('ConcreteClass step3')
    def step4(self):
        print('ConcreteClass step4')


if __name__ == '__main__':

    concreteClass = ConcreteClass()
    concreteClass.templateMethod()
