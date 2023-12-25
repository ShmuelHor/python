# תרגיל 9: בדיקת מספר פלינדרום

txt ="Hello World"[::-1]
print(txt)

print("Enter a number to check if it is a palindrome number:",end=" ")
number = str(input())

#אני מחלק את אורך המערך לשתיים וקובע אותו כאינט כדי שיהיה בלי שארית
# הסיבה שאני מחלק את המערך לשתיים כי בבדיקה אני בודק מספר מהתחלה ומספר מהסוף
len = int(len(number) / 2)
End_Counter = 0
Counter = 0

# בודק האם המערך מחיל רק מספרים
if(number.isnumeric() == True):
    print("\n","original number:",number)
    
    for Start_Counter in range(0,len):
        End_Counter -= 1
# בודק האם האןת הרשונה מההתחלה ומהסוף אותו דבר וכך גם השני מהתחלה ומהסוף
        if(number[Start_Counter] == number[End_Counter] ):
            # הסיבה שאני מעלה באחד כי אם יש משהו אחד שלא דומה אז הוא לא יעלה 
            # וככה אני רואה שלא הכל דומה אחד לשני
            Counter += 1
        else:
            pass

    if(Counter == len):
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")
else:
    print("\n","Error: Please enter only numbers")

