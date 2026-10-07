class A:
    def display(self):
        print('Display called A.')
        
class B(A):
    def display(self):
        print('Display called B.')

class C(A):
    def display(self):
        print('Display called C.')
   
class D(B, C):
    pass

d = D()
d.display()

print(D.__mro__)
