#problem 1
class Block(Rectangle):
    def __init__(self, length = 0.0, width = 0.0 height = 0.0, ):
        Rectangle.__init__(self, length, width)
        self.__height = height

    def getVolume(self):
        return self.__height * self.getArea()


#problem 2:
def filter(infile,outfile):
    opening = open("macbeth.txt", "r")
    writing = open("new_file.txt", "w")

    while True:
        thisLine = opening.readline()
        theLine = theLine.split()
        if len(thisLine) == 0:
            break

        first_word = "I"
        if theLine[0] == first_word:
            writing.write(thisLine)

    opening.close()
    writing.close()

filter("macbeth.txt", "new_file.txt")


#translate into Java
