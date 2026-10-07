class Student:
    def __init__(self, rollno, name, city):
        self.rollno = rollno
        self.name = name
        self.city = city
    
    def display(self):
        print("Student Name: ", self.name)
        print("City: ", self.city)
        
    def __del__(self):
        print('Object deleted.')

s1 = Student(1, 'Prince', 'Rajkot')
s1.display()
del s1