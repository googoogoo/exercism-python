def convert(number):

    pling = ''
    plang = ''
    plong = ''

    if (number % 3 != 0) and (number % 5 != 0) and (number % 7 != 0):
        return str(number)
    else:
        if number % 3 == 0:
            pling = 'Pling'
        if number % 5 == 0:
            plang = 'Plang'
        if number % 7 == 0:
            plong ='Plong'
        return f"{pling}{plang}{plong}"
