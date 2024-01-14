
class ID():
    # This is the format of the calculation
    base = [1,2,1,2,1,2,1,2,1]
    # Override the array
    equals = [0,0,0,0,0,0,0,0,0]
    sum = 0
    def __init__(slaf,id):
        slaf.id = id

    def examination(slaf):

        for x in range(0,9):

            # I am multiplier the format by the id
            slaf.equals[x] += slaf.id[x] * slaf.base[x]

            # If the sum contains two numbers 
            if (slaf.equals[x] > 9):

                # then I add them together For example 12 = 1+2 =3 
                slaf.equals[x]= sum(map(int, str(slaf.equals[x])))
            # I add up all the numbers in the array
            slaf.sum += slaf.equals[x]
        # If the sum divisible by ten without remainder so the ID card is correct
        if (slaf.sum % 10) == 0:
            return True
        else:
            return False
        

def Conversion (txt):
    # לקחתי את המשתנה ןהוספתי רווחים בין כל אות
    result = ''
    for ch in txt:
        result = result + ch + ' '
    # אני לוקח כל ערך ושם אותו ברשימה
    list1 = result.split()
    # הפכתי את הרשימה למשתנה מסוג 
    list1 = list(map(int, list1))
    return list1

list1 = Conversion(str(input("Enter yor ID: ")))
c = ID(list1)
print("Yor ID is ",c.examination())
