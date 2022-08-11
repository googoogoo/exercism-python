import re
def abbreviate(words):

    regex = re.compile(r"[A-Z]+'?[A-Z]+|[A-Z]")
    return ''.join(word[0] for word in regex.findall(words.upper()))
