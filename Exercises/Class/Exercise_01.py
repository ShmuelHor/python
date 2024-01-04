class Vehicle:
    def __init__(self,max_speed,mileage ):
        self.max_speed = max_speed
        self.mileage = mileage
        
    def car(self):
        print("The Max Speed of The Car is: ",self.max_speed)
        print ("and The Mileage of The Car is:",self.mileage)
        
print("Enter The Max Speed of The Car")
max_speed = input()
print("Enter The Mileage of The Car")
mileage = input()
if(max_speed.isnumeric() and mileage.isnumeric()):
    x = Vehicle(max_speed,mileage)
    x.car()
else:
    pass
