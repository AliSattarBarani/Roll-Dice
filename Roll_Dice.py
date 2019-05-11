import random

class Dice:
    
    def __init__(self, name, levels):
            self.name = name
            self.levels = levels

    def rollDice(self):
        xwon = 0
        ywon = 0

        for i in range(self.levels):
            x = random.randint(1,6)
            print("Your Dice Value= ", x)
            y = random.randint(1,6)
            print("Opponent Dice Value= ", y)

            if x > y:
                print("Roll no. ", i+1)
                print(self.name + " " + "Won :)")
                print("End of the roll \n")
                xwon += 1 

            elif x == y:
                print("Roll no. ", i+1)
                print("No winner here!")
                print("End of the roll \n")

            else: 
                print("Roll no. ", i+1)
                print ("Opponent won :(")
                print("End of the roll \n")
                ywon += 1

        print("")
        print("Final Result")
        print("ــــــــــــــــــ")
        print(self.name + ":" + " " , xwon)
        print("Opponent" + ":" + " " , ywon)


name= input("Enter your name: \n")
levels = int(input("Enter no. of levels: \n"))
print("\n")

newDice = Dice(name, levels)
print(newDice.rollDice())

    