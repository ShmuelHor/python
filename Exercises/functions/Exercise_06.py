# תרגיל 6: יצירת פונקציה רקורסיבית
def tri_recursion(k):
  # 

  if(k > 0):
    last =  tri_recursion(k - 1)
    result = k + last
    print("K: " + str(k))
    print("last: " + str(last))
    print("result: " + str(result))
  else:
    result = 0
    
  return result

print("\n\nRecursion Example Results")
tri_recursion(10)
