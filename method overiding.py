#  It is a method having the same name with the same arguments

class A:
    def show(self):
        print("I am A")
class B(A):
    def show(self):
        print("I am B")

ob=B()

ob.show()
