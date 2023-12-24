# תרגיל 6: הצגת מספרים המתחלקים ב- 5 מתוך רשימה
# פה עשיתי שאפשאר לבחור גם באיזה מספר לחלק
print("Enter a list of 5 numbers")
x = [input(),input(),input(),input(),input()]
print("Please enter the divisor number")
n = input()
print("Given list is ",x,"\n")
for i in range(0,len(x)):
    # אני בודק האם הרשימה היא רק מכילה רק מספרים
    if(x[i].isnumeric() & n.isnumeric()):
        # בודק האם המספר מתחלק בחמש ללא ששארית
        if((int(x[i]) % int(n)) == 0):
            print(x[i])
        else:
            pass
    else:
        if(x.isnumeric() == False):
            print("Error in the license number Please enter numbers and no: ", x)
        elif(n.isnumeric() == False ):
            print("Error in the second number Please enter numbers and no: ",n)
        else:
            print("Error Please enter numbers and no: ",x,"and",n)
        pass