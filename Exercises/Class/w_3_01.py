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
    def __init__(self,fname,lname ,year):
# יש פונקציה שגורמת למחלקת הילד לרשת הכל ממחלקת האב
# לא צריך להשמש בשם האלמנט של האב הוא יורש הכל
        super().__init__(fname,lname)
# אפשר גם להוסיף מאפיינים
        self.GraduatioNyer = year
    def welcome(self):
        print("Welcome",self.FirstName,self.LastName,"to the class of",self.GraduatioNyer)

x = person("shmuel" , "horvitz")
x.PrintName()
       
x = Student("yoel" , "horvitz", 2024)
x.PrintName()

x.welcome()

