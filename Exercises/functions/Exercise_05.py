# תרגיל 5: יצירת פונקציה פנימית לחישוב התוספת
def aaa(a,b):
    def bbb (a,b):
       return a+b
    aa = bbb(a,b)
    return aa + 5

c = aaa(5,10)
print (c)