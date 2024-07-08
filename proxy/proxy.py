# -*- coding:utf-8 -*-
"""
代理模式
"""

from abc import ABC,abstractmethod

#图像接口【抽象角色】
class Image(ABC):
    @abstractmethod
    def display(self):
        pass
#图片【真实角色】
class RealImage(Image):
    def __init__(self,fileName) -> None:
        self.fileName = fileName

    def display(self):
        print('displaying  image {}'.format(self.fileName))

#代理图片【代理角色】
class ProxyImage(Image):
    def __init__(self,fileName,realImage) -> None:
        self.fileName = fileName
        self.image = realImage

    def display(self):
        self.image.display()

if __name__ == '__main__':

    proxyImage = ProxyImage('image1.png',RealImage('image1.png'))
    proxyImage.display()
