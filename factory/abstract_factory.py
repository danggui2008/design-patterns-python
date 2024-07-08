# -*- coding: utf-8 -*- 
"""
抽象工厂模式（Abstract Factory）
"""

from abc import ABC,abstractmethod

#操作系统【抽象产品（Abstract Product）】
class OperatingSystem(ABC):
    @abstractmethod
    def run(self):
        pass


#Windows操作系统【具体产品（Concrete Product）】
class WindowsOS(OperatingSystem):
    def run(self):
        print('running in windows os ')

class LinuxOS(OperatingSystem):
    def run(self):
        print('running in linux os ')
    


#应用程序【抽象产品（Abstract Product）】
class Application(ABC):
    @abstractmethod
    def open(self):
        pass

#word应用程序【具体产品（Concrete Product）】
class WordApplication(Application):
    def open(self):
        return print('打开word应用程序')

#excel应用程序【具体产品（Concrete Product）】 
class ExcelApplication(Application):
    def open(self):
        return print('打开Excel应用程序')
    


#软件工厂【抽象工厂（Abstract Factory）】
class SoftwareFactory(ABC):
    def createOperatingSystem(self):
        pass

    def createApplication(self):
        pass


#Window工厂【具体工厂（Concrete Factory）】
class WindowsSoftwareFactory(SoftwareFactory):
    def createOperatingSystem(self):
        return WindowsOS()
    
    def createApplication(self):
        return WordApplication()

#Linux工厂【具体工厂（Concrete Factory）】 
class LinuxSoftwareFactory(SoftwareFactory):
    def createOperatingSystem(self):
        return  LinuxOS()
    
    def createApplication(self):
        return ExcelApplication()
    



if __name__ == "__main__":
     windowsFactory = WindowsSoftwareFactory()
     windows = windowsFactory.createOperatingSystem()
     windowsApp = windowsFactory.createApplication()
     windows.run()
     windowsApp.open()

     linuxFactory = LinuxSoftwareFactory()
     linux = linuxFactory.createOperatingSystem()
     linuxApp = linuxFactory.createApplication()
     linux.run()
     linuxApp.open()