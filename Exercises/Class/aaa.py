class shmuel:
    def __init__(self, name, age):
        self.nam = name
        self.ag = age
        
    def __str__(self):
        return f"{self.nam}: {self.ag}"
        
p1 = shmuel("shmuel", 20)

print(p1)

