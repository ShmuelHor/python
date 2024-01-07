# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
from datetime import date

class Person():

    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
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
        
person1 = Person(input("Enter your full name: "),input("Enter your country of origin: "), date(int(input("Enter your date of birth, Year: ")),int(input("Days: ")),int(input("Months: "))))

print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.calculate_age())