# -*- coding: utf-8 -*- 
"""
 中介者模式
"""
from abc import ABC,abstractmethod

#ChatMediator【Mediator（抽象中介者）】
class ChatMediator(ABC):
    #通知接口：同事通过此接口与同事通信
    @abstractmethod
    def notify(self, name, message):
        pass

    @abstractmethod
    def register(self, colleague):
        pass
#ConcreteChatMediator【ConcreteMediator（具体中介者）】
class ConcreteChatMediator(ChatMediator):

    def __init__(self) -> None:
        self.colleagues = dict()

    def notify(self, name, message):
        #用户通知中介者，中价根据业务情况，完成相应的业务，这里调用同事的action方法完成业务
        if name in self.colleagues:
            colleague = self.colleagues.get(name)
            colleague.action(message)

    def register(self, colleague):
        self.colleagues[colleague.name] = colleague

#Colleague【Colleague（抽象同事类）】
class Colleague(ABC):
    def __init__(self,name) -> None:
        self.name = name

    @abstractmethod
    def action(self,message):
        pass

    @abstractmethod
    def sendMessage(self,message):
        pass

#ConcreteColleague【ConcreteColleague（具体同事类）】
class ConcreteColleague(Colleague):
    def __init__(self, name,mediator) -> None:
        super().__init__(name)
        self.__mediator = mediator

    def action(self, message):
        print('[{}]收到消息:{}，我马上行动起来'.format(self.name, message))


    def sendMessage(self, message):
        print('将要给[{}]发送消息:{}'.format(self.name,message))
        self.__mediator.notify(self.name, message)

if __name__ == '__main__':

    mediator = ConcreteChatMediator()
    colleague1 = ConcreteColleague('码海悔道', mediator)
    colleague2 = ConcreteColleague('小玉', mediator)
    colleague3 = ConcreteColleague('小李', mediator)
    
    mediator.register(colleague1)
    mediator.register(colleague2)
    mediator.register(colleague3)
    colleague1.sendMessage('月色真好')
    colleague2.sendMessage('来了')