import json
class computer:
    def __init__(self,color,memory,touch):
        self.color = color
        self.memory = float(memory)
        self.touch = touch
    def sumPrice(self):
        price = 1000
        if self.color == "blak":
            price += 50
        elif self.color == "selvar":
            price += 150
        elif self.color == "white":
            price += 100
        else:
            price += 200
        if self.memory == 0.5:
            price += 500
        elif self.memory == 1:
            price += 1000
        elif self.memory == 2:
            price += 1500
        else:
            print("memory is not exists")
        if self.touch == "yes":
            price += 999.99
        return price
def insrtPrint(color,memory,touch):
    dik_computer = {
        "color": color,
        "memory": memory,
        "touch": touch
    }
    x = computer(color,memory,touch)
    print(x.sumPrice())
    with open("my_data.json", "w") as json_file:
        json.dump(dik_computer, json_file)


def insrt(name_of_folder):
    with open(name_of_folder) as json_file:
         s1 = json.load(json_file)
    insrtPrint(s1["color"],s1["memory"],s1["touch"])
insrt("my_data.json")