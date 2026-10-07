class Student:
    #class variable
    clg = "Marwadi"
    
    #constructor
    def __init__(self, rollno, name):
        #instance variable
        self.name = name
        self.rollno = rollno
        
    #instance method
    def display(self):
        print("Instance method. Name: ", self.name)
    
    #Class method
    @classmethod
    def get_clg(cls):
        return cls.clg
    
    #static method
    @staticmethod
    def gen_enroll_no(rollno):
        return '9260058' + str(rollno)

s1 = Student(101, "Prince")
s1.display()

print('Calling Class method. College name : ', Student.get_clg())
print('Calling Static method. Enrollment no : ', Student.gen_enroll_no(s1.rollno))
