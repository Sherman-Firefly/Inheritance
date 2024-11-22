class vehicle:
    def __init__(self, name, speed, milage):
        self.name=name
        self.speed=speed
        self.milage=milage

class bus(vehicle):
    pass

schoolbus=bus("Blue Bird", 100, 10)
print("Vehicle brand name: ", schoolbus.name)
print("Vehicle max speed: ", schoolbus.speed)
print("Vehicle current milage: ", schoolbus.milage)