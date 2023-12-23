# תרגיל 3: הדפסת תווים ממחרוזת הנמצאים במספר אינדקס זוגי
"""כתוב תוכנית כדי לקבל מחרוזת מהמשתמש 
ולהציג תווים הנמצאים במספר אינדקס זוגי."""
print("Enter something ")
str = input()
print("\n","Orginal String is ",str) 
print("Printing only even index chars")     
for a in range(0,len(str),2):
    print(str[a])