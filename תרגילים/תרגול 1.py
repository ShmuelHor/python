def mere(): #סתם איזה שהיא פונקציהי
    global  myNane # אני מגדיר שיהיה אפשר להשתמש עם המשתנה מחוץ לתנאי
    myNane = ["shm","uel","hor"] # הוא כרגע מערך
    global x,y,z
    x,y,z = myNane # מפרק את המערך
mere() #נמר התנאי
print(x+y,z) # מדפיס
