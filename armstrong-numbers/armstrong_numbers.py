def is_armstrong_number(number):
    string_number = str(number)
    exp = len(string_number)
    arm = []
    for n in string_number:
       ns = int(n)
       ne = ns**exp
       arm.append(ne)
    armstrong = sum(arm)
    return number == armstrong
