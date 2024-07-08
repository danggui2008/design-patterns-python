# -*- coding: utf-8 -*- 
"""
 访问者模式
"""

from abc import ABC,abstractmethod
import math

#图形形状接口:accept接受访问者【Element类】
class Shape(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


#Circle【ConcreteElement类】
class Circle(Shape):
    def __init__(self,radius) -> None:
       self.radius = radius

    def accept(self, visitor):
        visitor.visitCircle(self)

#Rectangle【ConcreteElement类】
class Rectangle(Shape):

    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
    def accept(self, visitor):
         visitor.visitRectangle(self)
    

#图形访问者接口【抽象Visitor】
class ShapeVisitor(ABC):

    @abstractmethod
    def visitCircle(self, circle):
        pass

    @abstractmethod
    def visitRectangle(self, rectangle):
        pass

#AreaCalculator【Visitor类】
class AreaCalculator(ShapeVisitor):

    def __init__(self) -> None:
        self.area = 0.0

    def visitCircle(self, circle):
        self.area += math.pi * circle.radius * circle.radius
    
    def visitRectangle(self, rectangle):
        self.area += rectangle.width * rectangle.height

    def getArea(self): 
        return self.area
    

if __name__ == '__main__':

    circle = Circle(10.00)
    rectangle = Rectangle(10.00, 12.00)

    areaCalculator = AreaCalculator()
    circle.accept(areaCalculator)
    area = areaCalculator.getArea()
    print('circle area:{}'.format(area))
    
    rectangle.accept(areaCalculator)
    area = areaCalculator.getArea()
    print('total area:{}'.format(area))

