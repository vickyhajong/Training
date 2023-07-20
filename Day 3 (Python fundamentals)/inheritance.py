# Inheritance in Python
# Supports - Single, Multi-level, Multiple Inheritance

class BaseClass:
    def __init__(self) -> None:
        self.Id = 0
        self.Name = "Edgeverve"
        print("Baseclass.__init__called.")
    
    def show(self) -> None:
        print("BaseClass.show(ID:{0},Name:{1})".format(self.Id, self.Name))
## End of Base Class
class AnotherBase:
    pass

class DerivedClass(BaseClass):  #specify the name of the parent
    def __init__(self) -> None:
        super().__init__()      #invokes the parent/super initializer
        print('DerivedClass.__init__called.')

    
    def show(self) -> None:
        print("BaseClass.show(ID:{0},Name: {1})".format(self.Id, self.Name))

    
    def __eq__(self, __value: object) -> bool:
        return self.Id==__value.Id


###End of DerivedClass

bc = BaseClass()
bc.show()
dc = DerivedClass()
dc.show()
bc = dc
dc1 = DerivedClass()
print(dc == dc1)
dc1.Id = 122
print(dc == dc1)



######OPERATOR OVERLOADING ACHE SE SIKHLO###########

class TestCalss:
    def __inint__(self, id, name) -> None:
        self.Id = id
        self.Name = name
        print(self.Id, "--", self.Name)

t1 = TestClass(10,"Infy")
class TestDerived(TestClass):
    def __init__(self,id,name,location) -> None:
        super().__init__(id,name)
        self.Location = location

t2 = TestDerived(20,)        