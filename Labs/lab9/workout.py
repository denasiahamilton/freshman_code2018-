def rankAndSuitCount(cards):
    #index the cards because index 0 will be rank and index 1 is suit
    
    #rank
    rank = {'2': '2', '3': '3', '4': '4',
            '5': '5', '6': '6', '7': '7',
            '8': '8', '9': '9', 'T': 'T',
            'J': 'J', 'Q': 'Q', 'K': 'K',
            'A': 'A'}
    #suit
    suit = {'C': 'C', 'S': 'S', 'D': 'D', 'H': 'H'}

    the_occurance = { }
    for x in cards:
        the_occurance[x] = the_occurance.get(x, 0) + 1
    print(the_occurance)

rankAndSuitCount([ 'AS', 'AD', '2C', 'TH', 'TS' ])
