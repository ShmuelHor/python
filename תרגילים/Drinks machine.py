water = 9
orange = 8
apple = 4
cola = 4

x = input("Please enter the name of the drink: ")

if 'water' == x:
    print(water)
elif 'orange' == x:
    print(orange)
elif 'apple' == x or 'cola' == x:
    print(cola)
else:
    print("Non existent drink please enter again")

one = 0
two = 0
five = 0
ten = 0

x = input("Please enter the name of the drink: ")
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
    
    if y > 10:
        ten = (y // 10) - 1
        y -= ten * 10 
    else:
        pass

    if y > 5:
        five = (y // 5) -1
        y -=five * 5
    else:
        pass

    if y > 2:
        two = (y // 2) - 1
        y -= two * 2
    else:
        pass

    one = y // 1

    print("Your surplus in currencies is:")
    print(ten," coins of ten")
    print(five," coins of five")
    print(two," coins of two")
    print(one," coins of one")
elif y == 0:
    print("Thank you")
else:
    print("Put in more money ")
