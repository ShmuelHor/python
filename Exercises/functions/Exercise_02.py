# תרגיל 2: יצירת פונקציה עם אורך משתנה של ארגומנטים
def func1 (*a):
    print("Printing values")
    for i in a:
        print (i)
    print("\n")    
func1(20, 40, 60)

func1(80, 100)