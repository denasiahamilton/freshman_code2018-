#CSCI 1133 Homework2
#Denasia Hamilton
#Problem 2D

def main():
    player1_win = 0 #score keeper, player needs to win 2/3 rounds
    player2_win = 0 #score keeper, player needs to win 2/3 rounds
    count = 0
    rounds = 3
    while count in range(rounds): #plays 3 games
        count += 1
        print ("Round #", count)
        player1 = str(input("Player 1's Choice: "))
        player2 = str(input("Player 2's Choice: "))
        player1 = player1.lower() #non case-sensitive
        player2 = player2.lower() #non case-sensitive

        if player1 == "r" and player2 == "s":
            print("Player 1 wins this round")
            player1_win += 1

        elif player1 == "r" and player2 == "p":
            print("Player 2 wins this round")
            player2_win += 1

        elif player1 == "r" and player2 == "r":
            print("No one wins this round. It's a tie")

        elif player1 == "p" and player2 == "r":
            print("Player 1 wins this round")
            player1_win += 1

        elif player1 == "p" and player2 == "s":
            print("Player 2 wins this round")
            player2_win += 1

        elif player1 == "p" and player2 == "p":
            print("No one wins this round. It's a tie")

        elif player1 == "s" and player2 =="p":
            print("Player 1 wins this round")
            player1_win += 1

        elif player1 == "s" and player2 == "r":
            print("Player 2 wins this round")
            player2_win += 1

        elif player1 == "s" and player2 =="s":
            print("No one wins this round. It's a tie")

    if player1_win == 2 or player1_win == 3:
        print("Player 1 wins this game!")
    elif player2_win == 2 or player2_win == 3:
        print("Player 2 wins this game!")
    else:
        print("No one wins this game. You have to win at least 2/3 rounds. Play again!") #this accounts for ties

if __name__ == "__main__":
    main()
