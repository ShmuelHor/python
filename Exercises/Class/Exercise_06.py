# Exercise 6: Class Inheritance
# In a bus i have a rate of a 10%
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return f"{self.capacity * 100}"
    

class Bus(Vehicle):
    
    def fare(self):
# I am was have to exchange to float / int Because i have to divide
        sam = int(super().fare())
        sam += sam / 10
        return f"Total Bus fare is: {sam}"
    
        

School_bus = Bus("School Volvo", 12, 50)
print(School_bus.fare())

