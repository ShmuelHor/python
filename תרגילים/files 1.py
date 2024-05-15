import os
file_name = input()
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        print(file.read())
    answer = input("Do you want to overwrite the text? Answer yes or no :")
    if answer == "no":
        with open(file_name, "a") as file:
            file.write(input())
    else:
        with open(file_name, "w") as file:
            file.write(input())
else:
    with open(file_name, "w") as file:
        file.write(input())