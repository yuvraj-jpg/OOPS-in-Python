class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print(f"Mileage of Vehicle is {self.mileage}")
        print(f"Cost of Vehicle is {self.cost}")
        print("I am a vehicle")
        
class Car(Vehicle):
    def __init__(self,mileage,cost,tyre,hp):
        super().__init__(mileage,cost) # it calls constructor of base class
        self.tyre=tyre
        self.hp=hp
    def show_car_details(self):
        print(f"Tyres in Car is {self.tyre}")
        print(f"Horse Power in Car is {self.hp}")
        print("I am a Car")
ob=Vehicle("35KM","200")

c1=Car("24KM", "300",8,900)
c1.show_details()
c1.show_car_details()
