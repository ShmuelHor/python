# תרגיל 10: יצירת רשימה חדשה משתי רשימות באמצעות התנאי הבא
"""בהינתן שתי רשימות מספרים
, כתוב תוכנית ליצירת רשימה חדשה כך שהרשימה החדשה תכיל
 מספרים אי-זוגיים מהרשימה הראשונה ומספרים זוגיים מהרשימה השנייה."""
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list = []

for i in range(0,len(list1)):
    if(list1[i] % 2):
        list.append(list1[i])

for i in range(0,len(list2)):
    if(int(list2[i] % 2)== 0):
        list.append(list2[i])

print(list)

