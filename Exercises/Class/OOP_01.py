# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math

class Circle():
    def __init__(self,radius):
        self.radius = radius
        
    def Area_calculation(self):
        return math.pi * self.radius **2
    
    def Scope_calculation(self):
        return 2 * math.pi * self.radius
    
x = Circle(int(input("Please enter the radius of the circle: ")))

print("The area of the circle is:{:10.2f}".format(x.Area_calculation()))
print("The circumference of the circle is:{:10.2f}".format(x.Scope_calculation()))
