# -*- coding: utf-8 -*-
"""
命令模式
"""

from abc import ABC,abstractmethod

#Command命令【命令（Command）】
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

#LightOnCommand开灯命令【具体命令（Concrete Command）】
class LightOnCommand(Command):

    def __init__(self,light) -> None:
        self.light = light
    
    def execute(self):
        self.light.turnOn()


#LightOffCommand关灯命令【具体命令（Concrete Command）】
class LightOffCommand(Command):

    def __init__(self,light) -> None:
        self.light = light
    
    def execute(self):
        self.light.turnOff()


#Light灯【接收者（Receiver）】
class Light(object):
    def turnOn(self):
        print('Light is on')

    def turnOff(self):
        print('Light is off')

#RemoteControl【调用者/请求者（Invoker）】
class RemoteControl(object):

    def __init__(self,command = None) -> None:
        self.command = command
        
    def setCommand(self,command):
        self.command = command

    def pressButton(self):
        self.command.execute()

if __name__ == '__main__':
    #客户端（Client）
    #命令接收者
    light = Light ()
    #开灯命令
    lightOnCommand = LightOnCommand(light)
    #关灯命令
    lightOffCommand = LightOffCommand(light)
    #命令调用者：远程控制1
    control = RemoteControl()
    #设置开灯
    control.setCommand(lightOnCommand)

    control.pressButton()
    #设置关烟命令
    control.setCommand(lightOffCommand)
    control.pressButton()
