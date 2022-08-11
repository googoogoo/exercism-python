def score(word):
    # Create a dictionar where the keys are the letters and their scrabble score is their value    
    d = dict([
        ('a', 1),
        ('e', 1),
        ('i', 1),
        ('o', 1),
        ('u', 1),
        ('l', 1),
        ('n', 1),
        ('r', 1),
        ('s', 1),
        ('t', 1),
        ('d', 2),
        ('g', 2),
        ('b', 3),
        ('c', 3),
        ('m', 3),
        ('p', 3),
        ('f', 4),
        ('h', 4),
        ('v', 4),
        ('w', 4),
        ('y', 4),
        ('k', 5),
        ('j', 8),
        ('x', 8),
        ('q', 10),
        ('z', 10)
    ])

    t = 0
    #Transform all caracters in the word to lower case
    word = word.lower()

    #Loop through the word and the value of each word
    for letter in word:
        t += d[letter]
    #Return said value
    return t
