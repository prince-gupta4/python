class A:
    def display(self):
        print('Display called A.')
        
class B(A):
    def display(self):
        print('Display called B.')


d = B()
d.display()
