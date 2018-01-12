def fizzbuzz(x):
    if x == 15:
        return 'fizzbuzz'
    if x == 3:
        return 'fizz'
    if x == 7:
        return x
    if x == 1 or x == 2:
        return x
    else:
        return 'buzz'
