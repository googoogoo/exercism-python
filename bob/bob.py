import re
def response(hey_bob):
    hey_bob = re.sub(r'[^a-zA-Z0-9 \.!,?]', '', hey_bob)
    hey_bob = hey_bob.replace(' ','')
    if not hey_bob:
        return 'Fine. Be that way!'
    elif hey_bob[-1] == '?' and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob[-1] == '?' and not hey_bob.isupper():
        return 'Sure.'
    elif hey_bob[-1] != '?' and hey_bob.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
