#  It is possible to modilfy a method in child class that it has in herited from parent class. This is particularly useful in cases where the method inhertited from parent class does not fit in child class.In such cases, we re-implement the method in the child class this process of re-implementing a method in the child class is known as Method Overriding... 


class Bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("most of the Birds can fly but can not.")
class Sparrow(Bird):
    def flight(self):
        print("Sparrow Can Fly")
class Ostrich(Bird):
    def flight(self):
        print("Ostrich cannot Fly")
ob1=Bird()
ob2=Sparrow()
ob3=Ostrich()

ob3.flight()
