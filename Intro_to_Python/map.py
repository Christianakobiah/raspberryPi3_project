#names = ["Sam","John","James"]
#
#print(list(map(len,names)))

class Person:
    
    def __init__(self,age,name):
        self.age = age
        self.name = name
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
Christiana = Person(20, "Christiana")

    
print(Christiana.get_age() , Christiana.get_name())

