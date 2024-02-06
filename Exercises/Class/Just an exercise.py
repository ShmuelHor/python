# פתחתי סתם קלאס
class shmuel:
    # מעביר את הערכים שקיבלתי למשתנה אחר עם שייוך
    def __init__(self, name, age):
        self.name = name
        self.age = age
      # אני מחזיר את הערכים וכמובן יש פה את השיוך של המשתנה  
    def __str__(self):
        return f"{self.name}: {self.age}"
    # פה הפונקציה מבצעת פקודת הדפסה 
    def myfunc(self):
        print("Hello my name is: ",  self.name)

# זה שתי אפשרויות של הדפסה אני לא ראיתי הבדל בהדפסה

p1 = shmuel("shmuel", 36)
# פה אני משנה ערך
p1.age = 20
print(p1)

p1 = shmuel("John", 20)
p1.myfunc()

# כהה מוחקים נתונים כשנדפיס אז יקפוץ שגיאה

# p1 = shmuel("yoel", 45)
# פה זה מחיקה של ערך
# del p1.nam
# print(p1.nam, p1.ag)