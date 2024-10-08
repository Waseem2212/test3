# class Vehical:
#     def __init__(self,name):
#         self.name = name
    
# class Car(Vehical):
#     def __init__(self,name):
#         super().__init__(self,name)


class Vehical:
    def __init__(self,name):
        self.name = name
    def food(self):
        return f"The food of {self.name} s petrol"
class Person:
    def __init__(self,name):
        self.name = name
    def food(self):
        return f"The food of {self.name} s grass"
class Animal:
    def __init__(self,name):
        self.name = name
    def food(self):
        return f"The food of {self.name} s baryani"

# per = Person('Wasi')
# vhl = Vehical('car')
# anm = Animal('cow')