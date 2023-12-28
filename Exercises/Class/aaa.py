# פתחתי סתם קלאס
class shmuel:
    # מעביר את הערכים שקיבלתי למשתנה אחר עם שייוך
    def __init__(self, name, age):
        self.nam = name
        self.ag = age
      # אני מחזיר את הערכים וכמובן יש פה את השיוך של המשתנה  
    def __str__(self):
        return f"{self.nam}: {self.ag}"
    # פה הפונקציה מבצעת פקודת הדפסה 
    def myfunc(self):
        print("Hello my name is: " + self.nam)

# ההבדל בין שתי הפונקציות הם פה

# בפונקציה הזאות אני צריך למשוך כל ערך ולהדפיס        
p1 = shmuel("shmuel", 36)
p1.ag = 20
print(p1)

# והפונקציה השניה פשוט מדפיסה
p1 = shmuel("John", 20)
p1.myfunc()

# כהה מוחקים נתונים כשנדפיס אז יקפוץ שגיאה

# p1 = shmuel("yoel", 45)
# del p1.nam
# print(p1.nam, p1.ag)