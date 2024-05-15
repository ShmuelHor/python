num1 = input()
num2 = input()
try:
    with open("shmuel","w") as file:
        file.write(str(int(num1) * int(num2)))
except:
    with open("shmuel","w") as file:
        print("The input is no good")
        file.write(num1 + num2)
with open("shmuel","r") as file:
    print(file.read())