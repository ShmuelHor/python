# תרגיל 4: הסרת n תווים ראשונים ממחרוזת
"""כתוב תוכנית להסרת תווים ממחרוזת המתחילה מאפס עד 
n והחזרת מחרוזת חדשה."""
print("Enter a string")
str = input()
print("Enter a number but no more than the length of the string")
n = input()
# בדיקה האם המשתנה אן הוא מספר
if(n.isnumeric):
    # בדיקה האם אורך המחרוזת יותר קטנה מהמשתנה אן
    if(int(n) < int(len(str))):
        # הדפסה ממיקום אן עד סוף המחרוזת
        print(str[int(n) : int(len(str))])
    else:
        print("Error: Enter a number that is greater than the length of the string")
        pass
else:
    print("Error : You entered something that is not a number")
    pass

