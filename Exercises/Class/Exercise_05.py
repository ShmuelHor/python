# תרגיל 5: הגדר מאפיין שחייב להיות בעל אותו ערך עבור כל מופע מחלקה (אובייקט)
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def aaa(self):
        color = "white" 
        return f"Color: {color} | Vehicle name: {self.name} | Speed: {self.max_speed} | Mileage: {self.mileage}"

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

x = Car("School Volvo",180,12)
print(x.aaa())