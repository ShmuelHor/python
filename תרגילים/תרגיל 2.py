age = 20
txt = """py name is \"shmuel\" 
and i am \'{1}\' years old
and this string is the editor of \'{0}\' words """ #פה פתחתי מחרוזת של כמה שורות באמצעות """
length = len(txt) # הכנסתי את אורך המחרוזת לתוך משתנה
a = txt.upper() #הפכתי את כל האותיות לאותיות גדולות
b = a.replace("P","M") # תיקון של שגיאה במילה הרשאונה
c = b.format(length,age) # הכנסתי את המספרים לתוך מחרוזת עם מילים במקומות שהכנתי מראש
print(c) 

if "old" in txt: # פה אני בודק אם מילה מופיעה בתוך הטקסט 
    print("Yes")
else: # אחרת אם המילה לא ופיעה
    print("no")

print("old" in txt)
# יש אופציה לכסוך את כל  התנאי שעשיתי למעלה והוא מחזיר לך נכון או לא נכון
# שורה 2 \"shmuel\" זה אפשרות להדפיס עם הדגשה