# -*- coding: utf-8 -*- 
"""
单例模式
"""

import threading
class Singleton(type):
    _lock = threading.Lock()

    def __init__(self,*args,**kargs):
        self.__instance = None

    def __call__(self, *args, **kwds):
        if self.__instance is None:
            with self._lock:
                if self.__instance is None:
                    self.__instance = super().__call__(*args, **kwds)
                    return self.__instance
        else:
            return self.__instance
    
class MyClass(metaclass=Singleton):
    pass

def run():
    instance = MyClass
    print("thread_id:{},instance_id:{}".format(threading.get_ident(),id(instance)))

if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    print(a is b)

    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()