import math

class Circle():
    def __init__(self,radius):
        self.radius = radius
        
    def Area_calculation(self):
        return math.pi * self.radius **2
    
    def Scope_calculation(self):
        return 2 * math.pi * self.radius
 
class Triangle():
    def __init__(self, base, height, rib1, rib2):
        self.base = base
        self.height = height
        self.rib1 = rib1
        self.rib2 = rib2

    def Area_calculation(self):
        return 0.5 * self.base * self.height
        
    def Scope_calculation(self):
        return self.base + self.rib1 + self.rib2
    
class Square():
    def __init__(self,rib):
        self.rib = rib
     
    def Area_calculation(self):
        return self.rib * self.rib
        
    def Scope_calculation(self):
        return 4 * self.rib
    
class Rectangle():
    def __init__(self,long_rib,short_rib):
        self.long_rib = long_rib
        self.short_rib = short_rib
        
    def Area_calculation(self):
        return self.long_rib * self.short_rib
        
    def Scope_calculation(self):
        return self.long_rib * 2 + self.short_rib * 2 

    
circle = Circle(7)
print("The area of the circle is:{:10.2f}".format(circle.Area_calculation()))
print("The circumference of the circle is:{:10.2f}".format(circle.Scope_calculation()))

triangle = Triangle(8,9,12,12)
print("The area of the triangle is:",triangle.Area_calculation())
print("The circumference of the triangle is:",triangle.Scope_calculation())

square = Square(5)
print("The area of the square is:",square.Area_calculation())
print("The circumference of the square is:",square.Scope_calculation())

rectangle = Rectangle(7,4)
print("The area of the rectangle is:",rectangle.Area_calculation())
print("The circumference of the rectangle is:",rectangle.Scope_calculation())
