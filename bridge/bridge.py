# -*- coding: utf-8 -*- 
"""
桥接模式：将抽象与实现部分分离
"""

from abc import ABC,abstractmethod

class Color(ABC):

    @abstractmethod
    def applyColor(self):
        pass

#Red【具体实现（ConcreteImplementor）】
class Red(Color):
    def applyColor(self):
        print('applying red color')


#Blue【具体实现（ConcreteImplementor）】
class Blue(Color):
    def applyColor(self):
        print('applying blue color')


#shape接口【抽象（Abstraction）】

class Shape(ABC):
    def __init__(self,color=None) -> None:
        if color is not None:
            self.__color = color

    @property   
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color = color

    @abstractmethod
    def draw(self):
        pass


#Circle【修正抽象（RefinedAbstraction）】
class Circle(Shape):
    def draw(self):
        print('drawing a circle')
        self.color.applyColor()


#Square【修正抽象（RefinedAbstraction）】
class Square(Shape):
    def draw(self):
        print('drawing a square')
        self.color.applyColor()


if __name__ == '__main__':
    red = Red()
    circle = Circle()
    circle.color = red
    circle.draw()

    blue = Blue()
    square = Square()
    square.color = blue
    square.draw()
