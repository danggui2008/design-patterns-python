# -*- coding: utf-8 -*- 
"""
工厂方法
"""

from abc import ABC,abstractmethod

#图形接口【抽象产品（Abstract Product）】
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

#圆【具体产品（Concrete Product）】
class Circle(Shape):
    def draw(self):
       print('drawing a circle')

#Rectangle实现抽象产品
class Rectangle(Shape):
    def draw(self):
        print('drawing a rectangle')


#图形工厂抽象接口【抽象工厂（Abstract Factory）】
class ShapeFactory(ABC):
    @abstractmethod
    def createShape(self):
        pass

#圆工厂：负责创建圆形产品【具体工厂（Concrete Factory）】
class CircleFactory(ShapeFactory):
    def createShape(self):
        return Circle()

#矩形工厂：负责创建矩形产品【具体工厂（Concrete Factory）】 
class RectangleFactory(ShapeFactory):
    def createShape(self):
        return Rectangle()


if __name__ == '__main__':
    """
    CircleFactory只负责创建圆，RectangleFactory负责创建矩形，
    每种产品都有相应的工厂来创建，在新增产品时，只需要新增相应
    的工厂就可，做到了“开闭原则”。
    """
    factory1 = CircleFactory()
    factory2 = RectangleFactory()
    circle = factory1.createShape()
    circle.draw()
    rectangle = factory2.createShape()
    rectangle.draw()