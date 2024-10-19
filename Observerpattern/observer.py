from abc import ABCMeta,abstractmethod

class Observer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self,*args,**kwargs):
        pass

