# תרגיל 8: הדפס את התבנית הבאה
#   משולש של זוית 90 מעלות של מספרים או כל צורה אחרת
print("Enter which object you want to print:")
print(  "If you want to print a pyramid of numbers in order") 
print("enter the word 'number':",end=" ")
b = input()
print("Enter the amount of objects you want to print",end=" ") 
number = input()
# דבר רשאון אני בודק האם המונה זה מספר
if(number.isnumeric() == True):
# ואז אני מריץ לולאה רשאונה
    for i in range(int(number)+ 1):
# ובתוכו עוד לולאה שאחראית להדפיס כל מספר לפי הכמות של הספרה שלו
        for j in range(i):
            # אם אתה רוצה סתם להדפיס צורות או משהו אחר
            if(b != 'number'):
                print(b,end=' ')
                # אם אתה רוצה להדפיס פירמידה של מספרים
            else:
                print(i,end=" ")
                # וזה האחראי כל פעם להוריד אותי שורה
        print('')
else:
    print("Error: Please enter a number and not '",number,"'")