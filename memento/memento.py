# -*- coding: utf-8 -*- 
"""
 备忘录模式
"""
#Memento【Memento（备忘录）】
class Memento(object):
    def __init__(self,state) -> None:
        self.__state = state
    @property
    def state(self):
        return self.__state

#Originator【Originator（发起人】
class Originator(object):
    def __init__(self,state) -> None:
        self.__state = state
    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self,state):
        self.__state = state

    #以当前状态创建备忘录
    def createMemento(self):
        return Memento(self.__state)
    
    #根据备忘录来恢复状态
    def restoreMemento(self, memento): 
        self.__state = memento.state

    def show(self):
        print(self.__state)

class Caretaker(object):
    def __init__(self) -> None:
        self.mementos = []
    
    #添加备忘录
    def addMemento(self, memento):
        self.mementos.append(memento)
    

    #获取备忘录
    def getMemento(self, index):
        return self.mementos[index]

if __name__ =='__main__':

    #发起人
    originator = Originator('state 1')
    #创建备注录：state 1
    memento =  originator.createMemento()
    #负责人
    caretaker = Caretaker()
    caretaker.addMemento(memento)
    originator.state = 'state 2'
    #state 2
    originator.show()
    #恢复状态(state 2-》state 1)
    originator.restoreMemento(caretaker.getMemento(0))
    #已恢复到原来状态：state 1
    originator.show()

