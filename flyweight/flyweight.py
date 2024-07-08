# -*- coding:utf-8 -*-
"""
享元模式
"""

from abc import ABC,abstractmethod

#Shape【抽象享元角色（Flyweight）】
class Shape(ABC):

    @abstractmethod
    def draw(self, coordinate):
        pass

#Color颜色【内部状态】
class Color(object):
    def __init__(self,color) -> None:
        self.color = color

#Coordinate坐标【外部状态】
class Coordinate(object):
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
"""
Circle【具体享元角色（Concrete Flyweight）】
圆：画一个圆包括：坐标，颜色
这里我们假设颜色只有：红、绿、蓝，黄，而坐标不固定。
那么圆的坐标适合作为对象的外部状态，而颜色为：内部状态。
"""
class Circle(Shape):
    
    def __init__(self,color) -> None:
        self.color = color

    def draw(self, coordinate):
         print('Draw a {} color circle at x:{},y:{}'.format(self.color.color,coordinate.x,coordinate.y))

#ShapeFactory【元工厂（Flyweight Factory）】
class ShapeFactory:

    def __init__(self) -> None:
        self.shapes = dict()

    def getShape(self,color):
        if color in self.shapes:
            return self.shapes.get(color)
        else:
            circle = Circle(Color(color))
            self.shapes[color] = circle
            return circle
    

if __name__ == '__main__':
    
    factory = ShapeFactory()
    colors = ['red', 'green', 'blue', 'yellow']
    for i in range(0,10):
        for c in range(0,4):
            x = (i + c + 10)
            y = (i + c + 20)
            #对象外部状态：坐标
            coordinate = Coordinate(x, y)
            shape = factory.getShape(colors[c])
            shape.draw(coordinate)
    
