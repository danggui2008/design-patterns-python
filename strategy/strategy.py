# -*- coding: utf-8 -*- 
"""
 策略模式
"""
from abc import ABC,abstractmethod

#MathOperation【抽象策略类（Strategy）】
class MathOperation(ABC):
    @abstractmethod
    def operate(self, a, b):
        pass


#Addition【具体策略类ConcreteStrategy】
class Addition(MathOperation):
    def operate(self, a, b):
        return a + b

#Subtraction【具体策略类ConcreteStrategy】
class Subtraction(MathOperation):
    def operate(self, a, b):
        return a - b

#Multiplication【具体策略类ConcreteStrategy】
class Multiplication(MathOperation):
    def operate(self, a, b):
        return a * b


#Calculator【上下文Context】
class Calculator:
   def __init__(self,operation = None) -> None:
       self.operation = operation

   def setOperation(self,operation):
       self.operation = operation

   def performOperation(self, a, b):
        return self.operation.operate(a, b)
    

if __name__ == '__main__':

    calculator = Calculator(Addition())
    result = calculator.performOperation(20.2, 550.20)
    print('result:{}'.format(result))
    calculator.setOperation(Subtraction())
    result = calculator.performOperation(99.90, 88.52)
    print('result:{}'.format(result))

    calculator.setOperation(Multiplication())
    result = calculator.performOperation(100.00, 88.52)
    print('result:{}'.format(result))

