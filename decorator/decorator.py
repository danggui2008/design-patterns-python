# -*- coding: utf-8 -*-
"""
装饰器模式
"""

from abc import ABC,abstractmethod

#咖啡接口【组件（Component）】
class Coffee():

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def desc(self):
        pass

#普通咖啡【具体组件（Concrete Component）】
class SimpleCoffee(Coffee):
    def cost(self):
        return 10
    
    def desc(self):
        return 'Simple Coffee'

#CoffeeDecorator接口【装饰器（Decorator)】
class CoffeeDecorator(Coffee):
    def __init__(self,coffee) -> None:
        self.__coffee = coffee

    def cost(self):
        return self.__coffee.cost()
    
    def desc(self):
        return self.__coffee.desc()

#MilkDecorator【具体装饰器（Concrete Decorator）】  
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return  super().cost() + 2
    def desc(self):
        return '{} ,with  Milk'.format(super().desc())

#SugarDecorator【具体装饰器（Concrete Decorator）】
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return  super().cost() + 2
    def desc(self):
        return '{} ,with  Sugar'.format(super().desc())



if __name__ == '__main__':

    #普通咖啡
    simpleCoffee = SimpleCoffee()
    print('花了{}(元)，买了一杯{}'.format(simpleCoffee.cost(),simpleCoffee.desc()))
       
    #加牛奶的咖啡
    milkDecorator = MilkDecorator(simpleCoffee)
    print('花了{}(元)，买了一杯{}'.format(milkDecorator.cost(),milkDecorator.desc()))
    #给牛奶的咖啡加点糖
    sugarDecorator = SugarDecorator(milkDecorator)
    print('花了{}(元)，买了一杯{}'.format(sugarDecorator.cost(),sugarDecorator.desc()))
