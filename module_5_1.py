class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor


    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floor:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


my_house = House("ЖК Эльбрус", 30)
my_house1 = House("Домик в деревне", 3)
my_house.go_to(7)
my_house1.go_to(4)
