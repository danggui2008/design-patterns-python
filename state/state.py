# -*- coding: utf-8 -*- 
"""
 状态模式
"""
from abc import ABC,abstractmethod

#ElevatorState【抽象状态角色（State）】
class ElevatorState(ABC):
    @abstractmethod
    def openDoor(self):
        pass

    @abstractmethod
    def closeDoor(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass

#ElevatorState电梯开门状态【具体状态角色（ConcreteState）】
class OpenState(ElevatorState):
    def openDoor(self):
        print('door is already opened')
    
    def closeDoor(self):
        print('closing the door')
    
    def move(self):
        print('cannot move while is the door is opened')
    
    def stop(self):
        print("is stopped")
    
#CloseState电梯关门状态【具体状态角色（ConcreteState）】
class CloseState(ElevatorState):
    def openDoor(self):
        print('opening the door')

    
    def closeDoor(self):
        print('the door is closed')
    
    def move(self):
        print('moving')
    
    def stop(self):
        print('stopping')
    
#Elevator电梯【环境角色（Context）】
class Elevator(object):
    def __init__(self,state = None) -> None:
        self.state = state

    def setState(self,state):
        self.state = state

    def openDoor(self):
        self.state.openDoor()
        self.state = OpenState()
    
    def closeDoor(self):
        self.state.closeDoor()
        self.state = CloseState()
    
    def move(self):
        self.state.move()
    
    def stop(self):
        self.state.stop()
    
if __name__ == '__main__':
    elevator = Elevator()
    #设置电梯为开门状态
    elevator.setState(OpenState())
    #开门
    elevator.openDoor()
    #门无法移动
    elevator.move()
    #关门
    elevator.closeDoor()
    #移动
    elevator.move()
    #停止
    elevator.stop()
    #开门
    elevator.openDoor()

