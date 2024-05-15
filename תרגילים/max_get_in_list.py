#המטרה של הקוד היא למצוא את המספר המקסימלי בכל רשימה מתוך רשימה של רשימות
def max_get(array):
    max_number = array[0]
    for i in range(1,len(array)):
        if max_number < array[i]:
            max_number = array[i]
    return max_number

def print_max_array(arrays):
    max_values = []
    for i in range(len(arrays)):
        max_values.append(max_get(arrays[i]))
    print(max_values)

def generate_array(n):
    array = []
    for i in range(n):
        array.append(int(input()))
    return array

arrays = []
for i in range(5):
    arrays.append(generate_array(4))
print_max_array(arrays)