class Student:
    #class variable
    clg = "Marwadi"
    
    def __init__(self, name):
        #instance variable
        self.name = name

s1 = Student('Prince')

print("Instance variable: ", s1.name)
print("Class varible, access with object : ", s1.clg)
print("Class varible, access with Class : ", Student.clg)