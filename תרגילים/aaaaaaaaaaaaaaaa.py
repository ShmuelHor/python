def find_min(a):
    x = 0
    min_num = a[0]
    for i in range(len(a)):
        if a[i] < min_num:
            min_num = a[i]
            x = i
    return x

def swap(a,i,j):
    a[i], a[j] = a[j], a[i]
    return a

a = [14, 7, 46, 33, 8, 5, 67]
for i in range(len(a)):
    min_index = find_min(a[i:]) +i
    swap(a,i,min_index)
print(a)

