import re

def count_words(sentence):
    
    regex = re.compile(r"[a-z]+'?[a-z]+|\d+|[a-z]")
    
    word_count = {}

    for word in regex.findall(sentence.lower()):
        word_count.setdefault(word, 0)
        word_count[word] += 1

    return word_count

