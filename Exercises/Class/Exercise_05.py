# תרגיל 5: הגדר מאפיין שחייב להיות בעל אותו ערך עבור כל מופע מחלקה (אובייקט)
class Vehicle:
    # Static variables are allocated memory once when the object for the class is created for the first time.
    # Static variables are created outside of methods but inside a class
    color = "white"
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    # Print the content of the class
    def Print(self): 
        return f"Color: {color} | Vehicle name: {self.name} | Speed: {self.max_speed} | Mileage: {self.mileage}"

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

car = Car("School Volvo",180,12)
print(car.Print())
