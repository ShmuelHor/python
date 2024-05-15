def optimized_sort(arr):
# מיון בועות
    for i in range(len(arr)-1):
        for g in range(len(arr)-(i+1)):
            if arr[g] > arr[g+1]:
                arr[g],arr[g+1] = arr[g+1],arr[g]
    return arr
def  selection_sort(arr):
    #מיון_בחירה
    for i in range(len(arr)):
        min_index = i
        for g in range(i,len(arr)):
            if arr[min_index] > arr[g]:
                min_index = g
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(optimized_sort(arr))
print(selection_sort(arr))

def aaa(num):
    # סכום מכפלה של כל הספרות
    if num < 10:
        return num
    else:

        return num % 10 * aaa(num // 10)
print(aaa(2232))