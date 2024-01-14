import random
    
class ID():
    # This is the format of the calculation
    base = [1,2,1,2,1,2,1,2]
    # Override the array
    equals = [0,0,0,0,0,0,0,0]
    sum = 0
    def __init__(slaf,id):
        slaf.id = id

    def examination(slaf):

        for x in range(0,8):

            # I am multiplier the format by the id
            slaf.equals[x] += slaf.id[x] * slaf.base[x]

            # If the sum contains two numbers 
            if (slaf.equals[x] > 9):

                # then I add them together For example 12 = 1+2 =3 
                slaf.equals[x]= sum(map(int, str(slaf.equals[x])))
            # I add up all the numbers in the array
            slaf.sum += slaf.equals[x]
            # Here I add the check digit for the ID
        if (slaf.sum % 10) != 0:
            if slaf.sum < 20:
                slaf.id.append(20 - slaf.sum)
            elif 20 < slaf.sum < 30:
                slaf.id.append(30 - slaf.sum)
            elif 30 < slaf.sum < 40:
                slaf.id.append(40 - slaf.sum)
            elif 40 < slaf.sum < 50:
                slaf.id.append(50 - slaf.sum)
            elif 50 < slaf.sum < 60:
                slaf.id.append(60 - slaf.sum)
            elif 60 < slaf.sum < 70:
                slaf.id.append(70 - slaf.sum)
            elif 70 < slaf.sum < 80:
                slaf.id.append(80 - slaf.sum)
            else:
                slaf.equals.append(0)
        return slaf.id

my_randoms=[]
for i in range (8):
    # Here I put the random numbers for the ID card
    my_randoms.append(random.randrange(1, 10, 1))
    
x = ID(my_randoms)
print("Yor ID is: ",x.examination())
        

