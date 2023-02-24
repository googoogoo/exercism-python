def is_valid(isbn):
    clean = isbn.replace('-', '')
    if len(clean) != 10:
        return False
    if clean[-1] == 'X':
        clean = clean.replace('X', '10')
    for c in clean:
        if c.isalpha():
            return False
    if len(clean) == 11:
        return (int(clean[0]) * 10 + int(clean[1]) * 9 + int(clean[2]) * 8 + int(clean[3]) * 7 + int(clean[4]) * 6 + int(clean[5]) * 5 + int(clean[6]) * 4 + int(clean[7]) * 3 + int(clean[8]) * 2 + 10) % 11 == 0
    else:
        return (int(clean[0]) * 10 + int(clean[1]) * 9 + int(clean[2]) * 8 + int(clean[3]) * 7 + int(clean[4]) * 6 + int(clean[5]) * 5 + int(clean[6]) * 4 + int(clean[7]) * 3 + int(clean[8]) * 2 + int(clean[9])) % 11 == 0
