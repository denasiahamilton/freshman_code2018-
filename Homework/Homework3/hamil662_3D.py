#CSCI 1133 Homework 3
#Denasia Hamilton
#Problem 3D

# Tic-Tac-Toe table
def table(n, init, player1, player2):
    player1_letter = "x"
    player2_letter = "o"
    empty_list = [ ]
    row = 0
    for row in range(n):
        row += 1
        new_list = [ ]
        empty_list.append(new_list)
        for column in range(n):
            second_list = init
            new_list.append(second_list)

    if player1 == 0:
        del empty_list[0][0]
        empty_list[0].insert(0, player1_letter)

    elif player1 == 1:
        del empty_list[0][1]
        empty_list[0].insert(1, player1_letter)

    elif player1 == 2:
        del empty_list[0][2]
        empty_list[0].insert(2, player1_letter)

    elif player1 == 3:
        del empty_list[1][0]
        empty_list[1].insert(0, player1_letter)

    elif player1 == 4:
        del empty_list[1][1]
        empty_list[1].insert(1, player1_letter)

    elif player1 == 5:
        del empty_list[1][2]
        empty_list[1].insert(2, player1_letter)

    elif player1 == 6:
        del empty_list[2][0]
        empty_list[2].insert(0, player1_letter)

    elif player1 == 7:
        del empty_list[2][1]
        empty_list[2].insert(1, player1_letter)

    elif player1 == 8:
        del empty_list[2][2]
        empty_list[2].insert(2, player1_letter)

    if player2 == 0:
        del empty_list[0][0]
        empty_list[0].insert(0, player2_letter)

    elif player2 == 1:
        del empty_list[0][1]
        empty_list[0].insert(1, player2_letter)

    elif player2 == 2:
        del empty_list[0][2]
        empty_list[0].insert(2, player2_letter)

    elif player2 == 3:
        del empty_list[1][0]
        empty_list[1].insert(0, player2_letter)

    elif player2 == 4:
        del empty_list[1][1]
        empty_list[1].insert(1, player2_letter)

    elif player2 == 5:
        del empty_list[1][2]
        empty_list[1].insert(2, player2_letter)

    elif player2 == 6:
        del empty_list[2][0]
        empty_list[2].insert(0, player2_letter)

    elif player2 == 7:
        del empty_list[2][1]
        empty_list[2].insert(1, player2_letter)

    elif player2 == 8:
        del empty_list[2][2]
        empty_list[2].insert(2, player2_letter)

    for x in empty_list:
        print(x)

# I had trouble making the while loop continue until all spaces were full (so 9 times)
# Or until there were 3 in a row
def main():
    track = [ ]

    player1 = int(input("Player 1, where do you want to move? "))
    track.append(player1)

    isValid = True
    while isValid:
        isValid = False
        player2 = int(input("Player 2, where do you want to move? "))
        if player2 not in track:
            track.append(player2)
        else:
            print("Sorry, that spot is taken")
            isValid = True

    table(3, " ", player1, player2)
if __name__ == "__main__":
    main()


# Needed a new function, these would print result of game
"""
#ROW
if empty_list[0][0] and empty_list[0][1] and empty_list[0][2] == "x":
    print(Player1 wins!!!)
elif if empty_list[0][0] and empty_list[0][1] and empty_list[0][2] == "o":
    print(Player2 wins!!!)
elif empty_list[1][0] and empty_list[1][1] and empty_list[1][2] == "x":
    print(Player1 wins!!!)
elif empty_list[1][0] and empty_list[1][1] and empty_list[1][2] == "o":
    print(Player2 wins!!!)
elif empty_list[2][0] and empty_list[2][1] and empty_list[2][2] == "x":
    print(Player1 wins!!!)
elif empty_list[2][0] and empty_list[2][1] and empty_list[2][2] == "o":
    print(Player2 wins!!!)

# COLUMN
elif empty_list[0][0] and empty_list[1][0] and empty_list[2][0] == "x":
    print(Player1 wins!!!)
elif empty_list[0][0] and empty_list[1][0] and empty_list[2][0] == "o":
    print(Player2 wins!!!)
elif empty_list[0][1] and empty_list[1][1] and empty_list[2][1] == "x":
    print(Player1 wins!!!)
elif empty_list[0][1] and empty_list[1][1] and empty_list[2][1] == "o":
    print(Player2 wins!!!)
elif empty_list[0][2] and empty_list[1][2] and empty_list[2][2] == "x":
    print(Player1 wins!!!)
elif empty_list[0][2] and empty_list[1][2] and empty_list[2][2] == "o":
    print(Player2 wins!!!)

#ACROSS
elif empty_list[0][0] and empty_list[1][1] and empty_list[2][2] == "x":
    print(Player1 wins!!!)
elif empty_list[0][0] and empty_list[1][1] and empty_list[2][2] == "o":
    print(Player2 wins!!!)
elif empty_list[0][2] and empty_list[1][1] and empty_list[2][0] == "x":
    print(Player1 wins!!!)
elif empty_list[0][2] and empty_list[1][1] and empty_list[2][0] == "o":
    print(Player2 wins!!!)
else:
    print("No one wins, it's a tie! Play again!!!")
"""
