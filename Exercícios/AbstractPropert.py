from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    @abstractmethod
    def name(self):
        ...
   

class Foo(AbstractFoo):
    name = ' '

    def __init__(self, name):
        super().__init__(name)
        #print('Foo criado')
    
     


foo = Foo('Luiz')
print(foo.name)