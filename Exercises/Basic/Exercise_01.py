# תרגיל 1: חשב את הכפל והסכום של שני מספרים
""" בהינתן שני מספרים שלמים,
 החזר את המוצר שלהם רק אם המוצר שווה או נמוך מ-1000. אחרת
החזר את הסכום שלהם"""
# קלט של שתי מספרים
print("Please enter the license number")
x = input()
print("Please enter the second number")
y = input()

# אני בודק האם הקלט הוא מספר
if(x.isnumeric() & y.isnumeric()):
    print("number1 = ", x)
    print("number2 = ", y ,"\n")
    # עכשו אני בודק האם הכפל של המספרים הוא מעל 1000
    if(int(x) * int(y) > 1000):
        print("The result is: " , int(x) + int(y),"\n")
    else:
        print("The result is: " , int(x) * int(y),"\n")
else:
    # איתור השגיאה
    if(x.isnumeric() == False):
        print("Error in the license number Please enter numbers and no: ", x)
    elif(y.isnumeric() == False ):
        print("Error in the second number Please enter numbers and no: ",y)
    else:
        print("Error Please enter numbers and no: ",x,"and",y)
    pass

