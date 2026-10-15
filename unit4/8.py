from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def accelerate(self):
        pass
    
    @abstractmethod
    def put_break(self):
        pass
    
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        
    def accelerate(self):
        print("Car accelerating...")
        
    def put_break(self):
        print("Car putting break...")
    
c = Car()
c.accelerate()
c.put_break()