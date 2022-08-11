class Luhn:
    def __init__(self, card_num):
        #Remove with spaces
        self.string = card_num.replace(' ','')
            
    def valid(self):
        digits = self.string

        #Check if input is larger than one and strictly numerical
        if len(digits) < 2:
            return False
        if digits.isdecimal() is False:
            return False

        total = 0
        #Loop through the values in the string, starting from the last and move towards the beggining of the string, two at a time
        for dig in digits[-1::-2]:
                value = int(dig)
                total += value

        #Loop through the values in the string, starting from the second to last and move towards the beggining of the string two at a time
        for dig in digits[-2::-2]:
                 value = int(dig)
                 double = value * 2
                 if double > 9:
                     double = double - 9
                 total += double

        #Test if the total is evenly divisible by ten
        return total % 10 == 0
