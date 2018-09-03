#CSCI 1133 Homework 6
#Denasia Hamilton
#Problem 6B

def parse_string(string):
    string = string.split()
    boring = ["to", "the", "and", "i", "of", "not",
              "he", "she", "a", "i'll", "i've",
              "but", "by", "we", "whose", "how",
              "go", "such", "this", "me", "can",
              "she's", "he's", "have", "has", "had",
              "an", "did", "so", "to", "we'll", "on",
              "him", "well", "or", "be", "as", "those",
              "there", "are", "do", "too", "if", "it",
              "at", "what", "my", "her", "his", "for",
              "is", "that", "you", "will", "in", "with"]

    #add words that are not in boring to dictionary
    d = { }
    for x in string:
        if x not in boring:
            count = string.count(x)
            if x.isalpha() == True:
                d[x] = count

    #pictogram -- change if/else statements (maybe needs to be nested)
    for x in d:
        stars = "* " * d[x]
        the_x = "X " * int(d[x] / 5)

        if d[x] < 5:
            print(x, stars)
        if d[x] % 5 == 0:
            print(x, the_x) #doesn't print for X if words are less than 5
        elif d[x] > 5 and d[x] % 5 != 0:
            mix = "* " * (d[x] % 5)
            print(x, the_x, mix)

def main():
    string = input("Enter a sentence or phrase: ")
    string = string.lower()
    for ch in ",.!:;~?)(\/|'-":
        string = string.replace(ch, "")
    parse_string(string)

if __name__ == '__main__':
    main()
