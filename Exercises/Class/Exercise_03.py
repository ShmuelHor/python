# תרגיל 3: צור מחלקת אוטובוס ומחלקת בן שיורשת את כל המשתנים והשיטות של מחלקת הרכב
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name) 
print("Speed:", School_bus.max_speed) 
print("Mileage:", School_bus.mileage)
