def is_reverse_ssort(array):
    for i in range(len(array)-1):
        if array[i] <= array[i+1]:
            return False
    return True
def flexible_search(array,n):
    if is_reverse_ssort(array):
        return binary_search(array,n)
    else:
        return search(array,n)

def binary_search(arr, n):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left + ((right - left)//2)
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            right = mid -1
        else:
            left = mid + 1
    return -1

def search(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1

arr = [1,7,3,8,4,9,3,6,3]
arr1 = [25,20,19,16,14,11,9,6,4,1]
print(flexible_search(arr1,14))
print(flexible_search(arr,6))