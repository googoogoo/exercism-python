def find_anagrams(word, candidates):    
    lower_word = word.lower()
    word_dict = {}
    for letter in lower_word:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1
    anagrams = []
    for candidate in candidates:
        lower_candidate = candidate.lower()
        if lower_word == lower_candidate:
            pass
        else:
            candidate_dict = {}
            for letter in lower_candidate:
                if letter in candidate_dict:
                    candidate_dict[letter] += 1
                else:
                    candidate_dict[letter] = 1
            if word_dict == candidate_dict:
                anagrams.append(candidate)
    return anagrams
