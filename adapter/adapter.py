# -*- coding: utf-8 -*- 
"""
适配器模式
"""

from abc import ABC,abstractmethod

#LegacyRectangle【源角色（Adaptee】
class LegacyRectangle(object):
    def display(self,x1,y1,x2,y2):
        print('LegacyRectangle({},{},{},{})'.format(x1,y1,x2,y2))

#Shape接口【目标角色（Target）】
class Shape(ABC):
    @abstractmethod
    def draw(self,x,y,width,height):
        pass

#RectangleAdapter【适配器（Adapter）】
class RectangleAdapter(Shape):
    def __init__(self) -> None:
        self.rectangle = LegacyRectangle()

    def draw(self, x, y, width, height):
        x2 = x + width
        y2 = y + height
        self.rectangle.display(x,y,x2,y2)



if __name__ == '__main__':
    shapeAdapter = RectangleAdapter()
    shapeAdapter.draw(10,10,100,50)