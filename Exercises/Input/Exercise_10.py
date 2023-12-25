# תרגיל 10: קרא את שורה מספר 4 מהקובץ הבא
x = open("C:\\Users\\shmue\\Downloads\\zxc.txt")
b = 0
for i in x:
    b += 1
    if(b == 4):
        print(i)
        break