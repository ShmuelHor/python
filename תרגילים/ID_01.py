import random
    
class ID():
    # This is the format of the calculation
    base = [1,2,1,2,1,2,1,2]
    # Override the array
    equals = [0,0,0,0,0,0,0,0]
    sum = 0
    x = 0
    calculator = 10
    def __init__(slaf,id):
        slaf.id = id

    def examination(slaf):

        for slaf.x in range(0,8):
            # I am multiplier the format by the id
            slaf.equals[slaf.x] += slaf.id[slaf.x] * slaf.base[slaf.x]

            # If the sum contains two numbers 
            if (slaf.equals[slaf.x] > 9):

                # then I add them together For example 12 = 1+2 =3 
                slaf.equals[slaf.x]= sum(map(int, str(slaf.equals[slaf.x])))
            # I add up all the numbers in the array
            slaf.sum += slaf.equals[slaf.x]
            
        # Here I add the check digit for the ID
        if (slaf.sum % 10) != 0:
            for e in range(9):
                slaf.calculator += 10

                if (slaf.calculator-10) < slaf.sum < slaf.calculator:
                    slaf.id.append(slaf.calculator - slaf.sum)
        else:
            slaf.id.append(0)          
        return slaf.id

my_randoms=[]
for i in range (8):
    # Here I put the random numbers for the ID card
    my_randoms.append(random.randrange(0, 10, 1))
    
x = ID([2,1,2,6,2,3,2,0])
print("Yor ID is: ",x.examination())
        

