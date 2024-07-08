# -*- coding: utf-8 -*- 
"""
 组合模式
"""
from abc import ABC,abstractmethod

#FileSystemComponent接口【组件（Component）】
class FileSystemComponent(ABC):
    
    @abstractmethod
    def displayInfo(self):
        pass

#File【叶子（Leaf）】
class File(FileSystemComponent):

    def __init__(self,name) -> None:
        self.name = name

    def displayInfo(self):
        print('File {}'.format(self.name))


#Directory【复合（Composite）】
class Directory(FileSystemComponent):

    def __init__(self,name) -> None:
        self.name = name
        self.__components = []

    def addComponent(self,component):
        self.__components.append(component)

    def displayInfo(self):
        print('Directory {}'.format(self.name))
        for c in self.__components:
            c.displayInfo()


if __name__ == '__main__':

    file1 = File("file1.txt")
    file2 = File("file2.txt")

    subDirectory = Directory("subDirectory")
    subDirectory.addComponent(file1)
    subDirectory.addComponent(file2)

    rootDirectory = Directory("root")
    rootDirectory.addComponent(subDirectory)
    rootDirectory.displayInfo()