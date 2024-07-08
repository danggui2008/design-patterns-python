# -*- coding: utf-8 -*- 
"""
 迭代器模式
"""
from abc import ABC,abstractmethod

class Iterator(ABC):

    def hasNext(self):
        pass

    def next(self):
 
        pass
class ConcreteIterator(Iterator):
    def __init__(self,items) -> None:
        self.items = items
        self.position = 0

    def hasNext(self):
        return len(self.items) > self.position

    def next(self):
        if self.hasNext():
            item = self.items[self.position]
            self.position +=1
            return item
        
class IterableCollection(ABC):

    @abstractmethod
    def createIterator(self):
        pass

class ConcreteCollection(IterableCollection):

    def __init__(self,items = None) -> None:
        self.items = []
        if items is not None:
            self.items.extend(items)

    def createIterator(self):
        return ConcreteIterator(self.items)

    def add(self,item):
        self.items.append(item)

if __name__ == '__main__':
    collection = ConcreteCollection()
    collection.add('A')
    collection.add('B')
    collection.add('C')
    
    
    iterator = collection.createIterator()
    while iterator.hasNext():
            print('item:{}'.format(iterator.next()))

