class MyClass:
    #fields
    text = "Infosys"
    codes = []


    def printDetails(): 
        print(MyClass.text)
        MyClass.codes =  [1,2,3,4]
        print(MyClass.codes)

MyClass.printDetails()
MyClass.text = "Edgeverve"
MyClass.printDetails()

# functon object dont have parameter as self in it whereas method oject do have self parameter in it
# '\' is used for continuation of line
# object as a parameter is sent whenever new object is created thats why we can use this or self keyword
class Product:
    ''' This is a sample class to demonstrate
        the Object Oriented behaviour of Python'''
    def __init__(self) -> None:
        self.productId = 1
        self.productName = 'Markers'
        self.price = 75.54
        self.__category = "Stationery"
    
    def printDetails(self):
        print(f"ID: {self.productId}, Name: {self.productName}, Price: {self.price}")
    
    def get_Name(self):   #getter method
        return self.productName
    def set_Name(self,value):    #setter method
        self.productName = value
    Name = property(get_Name, set_Name)

    @property
    def Category(self):
        return self.__category
    @Category.setter
    def Category(self, value):
        self.__category = value


p1 = Product() # --> Invokes the __init__ method
#object is created and a reference to the object is updated to p1
p1.printDetails()

p1.Name = "New Item"  #access the setter method
print(p1.Name)    #access the getter method
p1.__category = "New Category"
print(p1.__category)
p1.Category = "Updated"
print(p1.Category)
print(p1.__init__.__annotations__) # method annotations)
print(Product.__doc__)

''' Underscore in python
_variable --> normal variable name
__variable --> simulates a private field by mangling the field name as follows:
                ClassNmae__fieldname
__specialname__ --> Special type of method used to replace certain operations
            a+b ==> a.__add__(b)
            a == b ==> a.__eq__(b)'''






