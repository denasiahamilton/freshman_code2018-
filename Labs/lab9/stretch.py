
def morse():
    phrase = str(input("Enter a phrase: "))
    phrase = phrase.upper()
    phrase = list(phrase)
    print(phrase)

    the_code = {'A': '._',    'B': '_...',   'C': '_._.',
                'D': '-..',    'E': '.',      'F': '..-.',
                'G': '--.',    'H': '....',   'I': '..',
                'J': '.---',   'K': '-.-',    'L': '.-..',
                'M': '--',     'N': '-.',     'O': '---',
                'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	        'S': '...',    'T': '-',      'U': '..-',
                'V': '...-',   'W': '.--',    'X': '-..-',
                'Y': '-.--',   'Z': '--..'}

    for x in phrase:
        if x in the_code:
            print(the_code[x])

morse()
