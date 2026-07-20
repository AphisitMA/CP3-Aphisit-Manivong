class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")
class Car(Vehicle):
    def sayHello(self):
        print("Hello Car")
class Pickup(Vehicle):
    def sayHello(self):
        print("Hello Pickup")
class Van(Vehicle):
    def sayHello(self):
        print("Hello Van")
class EstateCar(Vehicle):
    def sayHello(self):
        print("Hello Estate Car")

car1 = Car()
car1.sayHello()
car1.turnOnAirConditioner()

car2 = Pickup()
car2.sayHello()
car2.turnOnAirConditioner()

car3 = Van()
car3.sayHello()
car3.turnOnAirConditioner()

car4 = EstateCar()
car4.sayHello()
car4.turnOnAirConditioner()
