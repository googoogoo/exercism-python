def flatten(iterable):
    flat = []
    for i in iterable:
        if type(i) == list:
            flat.extend(flatten(i))
        elif i is not None:
            flat.append(i)
    return flat
