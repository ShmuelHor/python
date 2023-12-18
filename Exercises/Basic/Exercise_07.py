# תרגיל 7: החזרת הספירה של תת-מחרוזת נתונה ממחרוזת
"""כתוב תוכנית כדי למצוא כמה פעמים
 תת-מחרוזת "Emma" מופיעה במחרוזת הנתונה."""
txt = "Emma is good developer. Emma is a writer"
txtt = "Emma"
i = 0
w = 0
p = -1 
while(i > -1):
    p = 1 + p
    i = txt.find(txtt,w)
    w = i + len(txtt)
print("Emma appeared", p ,"times")
