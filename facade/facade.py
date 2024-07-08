# -*- coding: utf-8 -*-
"""
门面模式
"""

#StereoSystem音响【子系统角色（SubSystem）】
class StereoSystem(object):

    def turnOn(self):
        print('打开音响')

    def turnOff(self):
        print('关闭音响')

#Projector投影仪【子系统角色（SubSystem）】
class Projector(object):

    def turnOn(self):
        print('打开投影仪')

    def turnOff(self):
        print('关闭投影仪')


#LightsControl灯光控制【子系统角色（SubSystem）】
class LightsControl(object):

    def turnOn(self):
        print('灯光已打开')

    def turnOff(self):
        print('灯光关闭')


#HomeTheaterFacade家庭影院外观【外观角色（Facade）】
class HomeTheaterFacade(object):

    def __init__(self) -> None:
        self.stereo = StereoSystem()
        self.projector = Projector()
        self.lights = LightsControl()

    def watchMovie(self):
        print('开始看电影')
        self.lights.turnOff()
        self.projector.turnOn()
        self.stereo.turnOn()

    def endMove(self):
        print('电影结束')
        self.stereo.turnOff()
        self.projector.turnOff()
        self.lights.turnOn()


if __name__ == '__main__':
    homeTheater = HomeTheaterFacade()
    #开始看电影
    homeTheater.watchMovie()
    #观影结束
    homeTheater.endMove()
