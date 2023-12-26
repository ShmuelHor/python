# לא הבנתי למה אמרת לי לפתוח כמה פונקציותזה עובד אפילו עם 2 
# אני בטוח שאפשר עם יותר
def aa(k):
  if(k > 0):
    result = k + bb(k - 1)
    print(result)
  else:
    result = 0
  return result

def bb(v):
  if(v > 0):
    result = v + aa(v - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
aa(10)
        
