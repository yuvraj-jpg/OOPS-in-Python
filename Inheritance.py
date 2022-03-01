class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print(f"Mileage of Vehicle is {self.mileage}")
        print(f"Cost of Vehicle is {self.cost}")
        print("I am a vehicle")
        
class Car(Vehicle):
    def show_car_details(self):
        print("I am a Car")
ob=Vehicle("35KM","200")

c1=Car("24KM", "300")
c1.show_details()
c1.show_car_details()
