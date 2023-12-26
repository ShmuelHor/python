# תרגיל 8: צרו רשימת פייתון של כל המספרים הזוגיים בין 4 ל-30
def Couple_Numbers(who,until,Duplicate):
    a = []

    for i in range(who,until,Duplicate):
        a += [i]
    print(a)

Couple_Numbers(4,32,2)
# זה הפיתרון אני הבנתי שצריך פונקציה אז השקעתי
print(list(range(4, 30, 2)))
# מה ההגדרה של הדבר הזה זה פונקציה ?
# או לולאה או סתם משהו