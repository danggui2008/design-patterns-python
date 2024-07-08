# -*- coding:utf-8 -*-
"""
解析器模式
"""

from abc import ABC,abstractmethod

#Expression【抽象表达式（Abstract Expression）】
class Expression(ABC):
    def interpret(self):
        pass

#NumberExpression【终结符表达式（Terminal Expression）】
class NumberExpression(Expression):
    def __init__(self,value) -> None:
        self.value = value
    def interpret(self):
        return self.value


#加法表达式AddExpression【非终结符表达式（Non-terminal Expression）】
class AddExpression(Expression) :
    def __init__(self,leftOperand,rightOperand) -> None:
        self.leftOperand = leftOperand
        self.rightOperand = rightOperand

    def interpret(self):
        return  self.leftOperand.interpret() + self.rightOperand.interpret()


#SubExpression减法表达式【非终结符表达式（Non-terminal Expression）】
class SubExpression(Expression) :
    def __init__(self,leftOperand,rightOperand) -> None:
        self.leftOperand = leftOperand
        self.rightOperand = rightOperand

    def interpret(self):
        return  self.leftOperand.interpret() - self.rightOperand.interpret()




if __name__ == '__main__':

    #3
    numberExpression = NumberExpression(3)
    #(10-3)
    subExpression = SubExpression(NumberExpression(10), NumberExpression(3))
    #3+(10-3)
    addExpression = AddExpression(numberExpression, subExpression)
    #10
    value = addExpression.interpret()
    print('value:{}'.format(value))
