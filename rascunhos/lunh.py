
class Luhn:
    def __init__(self, card_num):
        self.string = card_num.replace(' ','')

    def valid(self):
        digits = self.string
        #Check if input is larger than one and strictly numerical
        if len(digits) < 2:
            return False
        if digits.isdecimal() is False:
            return False
        #Reverse input and enumerate each digit
        inv_digits = digits[::-1]
        digits = enumerate(inv_digits)
        #Loop through inverted input and sum based on index
        total = 0
        for num, value in digits:
            value = int(value)
            if num % 2 == 0:
                total += value
            else:
                 double = value * 2
                 if double > 9:
                     double = double - 9
                 total += double
        return total % 10 == 0
