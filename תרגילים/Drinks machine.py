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

print("The total amount of the surplus is: ",y)

ten = y // 10
y -= ten * 10
five = y // 5
y -= five * 5
two = y // 2
y -= two * 2
one = y // 1
y -= one * 1
print("Your surplus in currencies is:")
print(ten," coins of ten")
print(five," coins of five")
print(two," coins of two")
print(one," coins of one")
