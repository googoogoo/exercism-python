def is_isogram(string):
    
    string = string.casefold().replace(' ', '').replace('-', '')
    duplicates = {}

    for char in string:
        if char in duplicates:
            duplicates[char] += 1
        else:
            duplicates[char] = 1
        
    for value in duplicates.values():
        if value > 1:
            return False
    return True
