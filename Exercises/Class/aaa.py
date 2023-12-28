class shmuel:
    def __init__(self, name, age):
        self.nam = name
        self.ag = age
        
    def __str__(self):
        return f"{self.nam}: {self.ag}"
    
    def myfunc(self):
        print("Hello my name is: " + self.nam)

        
p1 = shmuel("shmuel", 20)
print(p1)

p1 = shmuel("John", 36)
p1.myfunc()