
class Create_Prism(object):

    def __init__(self, length, width, height, ID):
        self.length = length
        self.width = width
        self.ID = ID
        self.height = height

    def __str__(self):
        strprint = "\nPrism ID: " + str(self.ID) + " units\n"
        strprint += "Length: "+ str(self.length) + " units\n"
        strprint += "Width: " + str(self.width) + " units\n"
        strprint += "Permimeter: " + str((self.width * 2) + (self.length * 2)) + " units\n"
        strprint += "Area: " + str((self.width) * (self.length)) + " units\n"
        strprint += "Volume: " + str((self.height) * (self.width) * (self.length)) + " units"
        strprint += "\n"
        return strprint


listofboxes = []
totalBoxes = 1
menu = """
        0 - Create A Prism
        1 - Print a Prism
        2 - Print all Prisms
        3 - Exit
        """

print(menu)

option = input("\nWhat would you like to do? (0-3): ")

listofboxes = []
totalBoxes = 1

while option != "3":

    
    if option == "0":
        length = int(input("Length: "))
        width = int(input("Width: "))
        height = int(input("Height: "))
        ID = totalBoxes

        if totalBoxes == 1:
            prism = Create_Prism(length, width, height, ID)
            listofboxes.append(prism)
        elif totalBoxes == 2:
            rectangle_2 = Create_Prism(length, width, height, ID)
            listofboxes.append(prism_2)
        elif totalBoxes == 3:
            rectangle_3 = Create_Prism(length, width, height, ID)
            listofboxes.append(prism_3)

        totalBoxes += 1
        print(menu)
        option = input("\nWhat would you like to do? (0-3): ")


    if option == "1":
        thisIsTrue = 1
        while thisIsTrue:
            try:
                if listofboxes:
                    print("There are " + str(len(listofboxes)) + " boxes already created.\n")
                else:
                    print("You have not created any prisms yet.")
                the_prism = int(input("Which one, (0-3) 0 being the first: "))
                print(listofboxes[the_prism])
                thisIsTrue = False
            except (IndexError, ValueError):
                print("That prism does not exist.")


        print(menu)
        choice = input("\nWhat would you like to do?: ")

    if option == "2":
        for i in listofboxes:
            print(i)

    print(menu)
    option = input("\nWhat would you like to do?: ")
