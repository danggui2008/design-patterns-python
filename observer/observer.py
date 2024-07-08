# -*- coding: utf-8 -*- 
"""
 备忘录模式
"""
from abc import ABC,abstractmethod


#Subject【抽象主题 (Subject)】
class Subject(ABC):
    @abstractmethod
    def addObserver(self, observer):
        pass

    @abstractmethod
    def removeObserver(self, observer):
        pass

    def notifyObservers(self):
        pass

#ConcreteSubject【具体主题 (Concrete Subject)】
class ConcreteSubject(Subject):
    def __init__(self,state) -> None:
        self.state = state
        self.__observers = []
   
    def addObserver(self, observer):
        self.__observers.append(observer)
    
    def removeObserver(self,observer):
        self.__observers.remove(observer)
    
    def notifyObservers(self):
        for observer in self.__observers:
           
            observer.update(self.state)

    def setState(self,state):
        self.state = state
       
#Observer【抽象观察者 (Observer)】
class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass

class ConcreteObserver(Observer):
   def __init__(self,id) -> None:
       self.id = id

   def update(self, state):
       print('Observer : {} state:{}is updated'.format(self.id,state))


if __name__ == '__main__':

    observer1 = ConcreteObserver(1)
    observer2 = ConcreteObserver(2)
    observer3 = ConcreteObserver(3)
    subject = ConcreteSubject(1)
    subject.addObserver(observer1)
    subject.addObserver(observer2)
    subject.addObserver(observer3)
    subject.setState(100)
    subject.notifyObservers()
    print('remove observer2')
    subject.removeObserver(observer2)

    subject.setState(200)
    subject.notifyObservers()
