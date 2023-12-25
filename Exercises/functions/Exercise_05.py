# תרגיל 5: יצירת פונקציה פנימית לחישוב התוספת

def outer(a,b):
    
    def Internal (a,b):
        return a + b
   
    Total = Internal(a,b)
    return Total + 5

c = outer(5,10)
print (c)