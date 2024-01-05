# תרגיל 4: ירושה מחלקתית
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
class Bus(Vehicle):
    # דריסת הפוקציה עם אותם משתנים, אבל בתוספת ערך ברירת מחדל
    # Source: https://www.w3schools.com/python/gloss_python_function_default_parameter.asp
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity) # אין צורך לחזור על ערך ברירת המחדל לדעתי

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity(11))
