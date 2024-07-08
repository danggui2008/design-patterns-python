# -*- coding:utf-8 -*-
"""
责任链模式
"""

from abc import ABC,abstractmethod


#报销请求
class ReimbursementRequest(object):
    def __init__(self,amount,desc) -> None:
        self.amount = amount
        self.desc = desc

#ReimbursementHandler【抽象处理角色（Handler）】
class ReimbursementHandler(ABC):

    @abstractmethod
    def handle(self,request):
        pass

#ManagerHandler经理【具体处理者角色（ConcreteHandler）】
class ManagerHandler(ReimbursementHandler):
    
    def __init__(self,name,successor=None) -> None:
        self.name = name
        self.successor = successor

    #经理处理报销:800以下可以处理
    def handle(self, request):
        if request.amount < 800.00: 
            print('经理:{}处理报销：{}元，报销情况：{}'.format(self.name,request.amount, request.desc))
                
        else:
            if self.successor is not None :
                self.successor.handle(request)
               
#DepartmentHeadHandler部门负责人【具体处理者角色（ConcreteHandler）】
class DepartmentHeadHandler(ReimbursementHandler):
    
    def __init__(self,name,successor=None) -> None:
        self.name = name
        self.successor = successor

    #部门处理报销:4000以下可以处理
    def handle(self, request):
        if request.amount < 4000.00: 
            print('部门主管:{}处理报销：{}元，报销情况：{}'.format(self.name,request.amount, request.desc))
                
        else:
            if self.successor is not None :
                self.successor.handle(request)
             

#财务能处理所有报销
class FinanceHandler(ReimbursementHandler):

    def __init__(self,name) -> None:
        self.name = name
    
    def handle(self, request):
        print('财务:{} 处理报销：{}元，报销情况：{}'.format(self.name, request.amount, request.desc))



if __name__ == '__main__':

    finance = FinanceHandler("小李")
    department = DepartmentHeadHandler("小强", finance)
    manager = ManagerHandler("小明", department)

    request1 = ReimbursementRequest(799.0, '王五北京出差高铁报销费用')
    request2 = ReimbursementRequest(3999.0, '王五上海出差8天住宿报销费用')
    request3 = ReimbursementRequest(4500.0, '王五杭州出差15天住宿报销费用')
   
    #经理能处理
    manager.handle(request1) 
    #经理不能处理，转给部门主管处理   
    manager.handle(request2)
    #经理不能处理，部分主管也不能处理，最后由财务处理
    manager.handle(request3)
