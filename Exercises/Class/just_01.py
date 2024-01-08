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
        
        today = date.today()
        
        if (today.month , today.day) <= (self.date_of_birth.month, self.date_of_birth.day):
            month = self.date_of_birth.month - today.month
            day = self.date_of_birth.day -  today.day
            
            if day < 0:
                month += -1
                day += 30
            return f"In {month} months and {day} days you will be "
        
        elif(today.month , today.day) > (self.date_of_birth.month, self.date_of_birth.day):
            month = self.date_of_birth.month - today.month
            day = self.date_of_birth.day -  today.day
            month += 11 
            day += 30
            if day < 0:
                month += -1
                day += 30
            return f"In {month} months and {day} days you will be "

        else:
            return f"aaaa"
        
        
person1 = Person(date(int(input("Enter your date of birth, Year: ")),int(input("Months: ")),int(input("Days: "))))
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.calculate_age())
print(person1.difference(),person1.calculate_age()+1,"years old")