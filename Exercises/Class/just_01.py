from datetime import date

class Person():
    
    def __init__(self,date_of_birth):
        self.date_of_birth = date_of_birth

    def calculate_age(self):
# פה אני מביא את התאריך של היום
        today = date.today()
# פה אני מוריד את השנת לידה פחות השנה של היום
        age = today.year - self.date_of_birth.year
# פה אני אומר אם התאריך לידה גדול מה תאריך של היום כולל ימים וחודשים אז תוריד שנה
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    
    def difference (self):
# אני מביא את הגיל שיצא בפונקציה הקודמת לפה
        x = Person.calculate_age(self)
# אני מביא את התאריך של היום
        today = date.today()
# מחשב בעוד כמה זמן אהיה לך יום הולדת
# אם התאריך של היום הולדת שלך גדול מהתאריך של היום אז
        if (today.month , today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            month = self.date_of_birth.month - today.month
            day = self.date_of_birth.day -  today.day
            
            if day < 0:
                month += -1
                day += 30
            return f"In {month} months and {day} days you will be {x + 1} years old"
# אם התאריך של היום הולדת שלך קטן מהתאריך של היום אז
        elif(today.month , today.day) > (self.date_of_birth.month, self.date_of_birth.day):
            month = self.date_of_birth.month - today.month
            day = self.date_of_birth.day -  today.day
            month += 11 
            day += 30
            if day < 0:
                month += -1
                day += 30
            return f"In {month} months and {day} days you will be {x + 1} years old "
# אם התאריך שווה אז
        else:
            return f"Happy Birthday"
        
        
person1 = Person(date(int(input("Enter your date of birth, Year: ")),int(input("Months: ")),int(input("Days: "))))
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.calculate_age())
print(person1.difference())