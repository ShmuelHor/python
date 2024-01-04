class Vehicle:
    def __init__(self,max_speed,mileage ):
        self.max_speed = max_speed
        self.mileage = mileage
        
    def car(self):
        print("The max speed of the car is: ",self.max_speed)
        print ("And the mileage of the car is:",self.mileage)
        
print("Enter the max speed of the car")
max_speed = input()
print("Enter the mileage of the car")
mileage = input()
if(max_speed.isnumeric() and mileage.isnumeric()):
    x = Vehicle(max_speed,mileage)
    x.car()
else:
    pass
