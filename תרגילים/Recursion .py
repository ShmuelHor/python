def aaaa(arr):
    #המטרה של הקוד היא למצוא זוג מספרים ברשימה שביניהם הסכום הגדול ביותר
    if len(arr) == 1:
        return arr
    else:
        n = len(arr) // 2
        left = aaaa(arr[:n])
        right = aaaa(arr[n:])
        return bbbb(left,right)
def bbbb(left,right):
    if left > right:
        return (right,left)
    return (left,right)
print(aaaa([6,3,1,7,2,0,7,8]))