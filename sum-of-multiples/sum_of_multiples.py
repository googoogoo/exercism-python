def sum_of_multiples(limit, multiples):
    factors = set()
    for number in multiples:
        if number == 0:
            continue
        else:
            for multiple in range(number, limit, number):
                factors.add(multiple)
    return sum(factors)
