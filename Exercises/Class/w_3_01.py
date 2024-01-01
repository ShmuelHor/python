# מחלקת האב
class person:
    def __init__(self,fname,lname):
        self.FirstName = fname
        self.LastName = lname
        
    def PrintName(self):
        print(self.FirstName , self.LastName)

# מחלקת הבן     
class Student(person):
# ברגע שאני מוסיפ את הפונקיצה הזאות אז מחלקת הבן לא תקרא לפונציה של מחלקת האב
    def __init__(self,fname,lname):
# פה אני קורא לפונקציה של מחלקת האב ואז ככה אני מושך נתונים מהפונקציה ממחלקת האב
        person.__init__(self,fname,lname)
        
x = person("shmuel" , "horvitz")
x.PrintName()
       
x = Student("yoel" , "horvitz")
x.PrintName()

