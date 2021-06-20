from abc import ABC,ABCMeta,abstractmethod
class MyBase(ABC):
    __metaclass__=ABCMeta
    @abstractmethod
    def show(self):
        pass
    class Derive(MyBase):
        def show(self):
            print("Show from device")

derive=Derive()
derive.show()
     #base=MyBase() #erro can't instantiate
