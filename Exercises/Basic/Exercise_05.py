# תרגיל 5: בדוק אם המספר הראשון והאחרון ברשימה זהים
print("Enter a list of 5 numbers")
x = [input(),input(),input(),input(),input()]
z = 0
# בדיקה האם זה מספר 
for i in range(0,len(x)):
    if(x[i].isnumeric()):
        # ואם זה מספר אז אני מעלה את המונה באחד
        z = z + 1
    else:
        break

# כאן אני בודק האם המונה שווה לאורך של הרשימה
    #כי אם הוא לא שווה סימן שהיא כאן ערך שהוא לא מספר
if(len(x) == z):
    print("\n","Given list ",x)
    # כאן אני בודק האם הערך הרשאון ברשימה שווה לערך האחרון ברשימה
    if(x[0] == x[-1]):
       print("result is True")
    else:
        print("result is False")
else:
    print("Error: Please enter only numbers in the list")