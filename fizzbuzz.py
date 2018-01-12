def fizzbuzz(x):
    str = ''
    if x % 3 == 0:
        str += 'fizz'
    if x % 5 == 0:
        str +='buzz'
    if x % 3 != 0 and x % 5 != 0:
        return x
    return str
