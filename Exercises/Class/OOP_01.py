# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle():
    pie = 3.14
    def __init__(self,radius):
        self.radius = radius
        
    def Area_calculation(self):
        Space = self.pie * self.radius * self.radius
        return f"The area of the circle is: {Space}"
    
    def Scope_calculation(self):
        scope = 2 * self.pie * self.radius
        return f"The circumference of the circle is: {scope}"
        
x = Circle(int(input("Please enter the radius of the circle: ")))
print(x.Area_calculation())
print(x.Scope_calculation())
