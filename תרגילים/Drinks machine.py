water = 9
orange = 8
apple = 4
cola = 4

x = input("Please enter the name of the drink: ")

if 'water' == x:
    print("The price is: ",water)
elif 'orange' == x:
    print("The price is: ",orange)
elif 'apple' == x or 'cola' == x:
    print("The price is: ",cola)
else:
    print("Non existent drink please enter again")

one = 0
two = 0
five = 0
ten = 0

a = int(input("Enter how many drinks you want to buy: "))
y = int(input("Please enter the amount of shekels you entered: "))

if 'water' == x:
    y -= water * a
    print("The drink you have chosen is water and the price is: ",water * a)
elif 'orange' == x:
    y -= orange * a
    print("The drink you have chosen is orange juice and the price is: ",orange * a)
elif 'apple' == x:
    y -= apple * a
    print("The drink you have chosen is apple juice and the price is: ",apple * a)
elif 'cola' == x:
    y -= cola * a
    print("The drink you have chosen is cola and the price is: ",cola * a)
else:
    print("Non existent drink please enter again")


if y > 0 :
    
    print("The total amount of the surplus is: ",y)
    
    if  y > 10:
        ten = y // 10 
        y -= ten * 10 

        if y < 8 :
            ten -= 1
            y += 10 
    else:
        pass

    if y > 5:
        five = y // 5 
        y -= five * 5 

        if y < 3 :
            five -= 1
            y += 5
    else:
        pass

    if y > 2:
        two = y // 2 
        y -= two * 2 

        if y < 1 :
            two -= 1
            y += 2
    else:
        pass

    one = y

    print("Your surplus in currencies is:")
    print(ten," coins of ten")
    print(five," coins of five")
    print(two," coins of two")
    print(one," coins of one")
elif y == 0:
    print("Thank you")
else:
    print("Put in more money ")
