# תרגיל 2: הדפס את סכום המספר הנוכחי והמספר הקודם
"""כתוב תוכנית לאייטרציה של 10 המספרים הראשונים
ובכל איטרציה הדפס את סכום המספר הנוכחי והקודם."""

y = 0

for x in range(0,10):
    sum = x + y
    print(" Current Number ",x," Previous Number " ,y, " Sum: ",sum)
    y = x 
