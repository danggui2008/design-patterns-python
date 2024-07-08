# -*- coding: utf-8 -*- 
"""
建造者模式
"""
from abc import ABC,abstractmethod

class House:
   
    def __init__(self) -> None:
        self.foundation = ''
        self.structure = ''
        self.roof = ''
        self.interior = ''
        
    def setFoundation(self,foundation):
        self.foundation = foundation

    def setStructure(self,structure):
        self.structure = structure
    
    def setRoof(self,roof):
        self.roof = roof
    
    def setInterior(self,interior):
        self.interior = interior

    def __str__(self) -> str:
        return "House({},{},{},{})".format(self.foundation,self.structure,self.roof,self.interior)
   


class HouseBuilder(ABC):
    @abstractmethod
    def buildFoundation(self):
        pass

    @abstractmethod
    def buildStructure(self):
        pass

    @abstractmethod
    def buildRoof(self):
        pass

    @abstractmethod 
    def buildInterior(self):
        pass

class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self) -> None:
        self.house = House()

    def buildFoundation(self):
        self.house.setFoundation('Standard Foundation')

    def buildStructure(self):
        self.house.setStructure('Standard Structure')

    def buildRoof(self):
        self.house.setRoof('Standard Roof')

    def buildInterior(self):
        self.house.setInterior('Standard Interior')


class LuxuryHouseBuilder(HouseBuilder):
    def __init__(self) -> None:
        self.house = House()

    def buildFoundation(self):
        self.house.setFoundation('Strong Foundation')
        
    def buildStructure(self):
        self.house.setStructure('Reinforced Structure')

    def buildRoof(self):
        self.house.setRoof('Reinforced Roof')

    def buildInterior(self):
        self.house.setInterior('Luxury Interior')

class Director(object):
    @staticmethod
    def constructHouse(builder):
        builder.buildFoundation()
        builder.buildStructure()
        builder.buildRoof()
        builder.buildInterior()
        return builder.house
    

if __name__ == '__main__':
   
    #建造普通房子
    houseBuilder1 = ConcreteHouseBuilder()
    house1 = Director.constructHouse(houseBuilder1)
    #建造好的房子
    print(house1)


    #建造豪宅
    houseBuilder2 = LuxuryHouseBuilder()
    house2 = Director.constructHouse(houseBuilder2)
    print(house2)
