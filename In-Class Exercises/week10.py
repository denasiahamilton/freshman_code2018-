class Pokemon:
    def __init__(self,nameIn):
        self.__name = nameIn
        self.__health = 100

    def setHealth(self,healthIn):
        self.__health = healthIn

    def getHealth(self):
        return self.__health

p1 = Pokemon("Pikachu")
p1HP = p1.getHealth()
p1HP = 85
p2 = Pokemon("Pikachu")
p3 = p2
p3.setHealth(75)
print(p1.getHealth(), p2.getHealth(), p3.getHealth())
