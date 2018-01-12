def fizzbuzz(x):
    words = ''
    if x % 3 == 0:
        words += 'fizz'
    if x % 5 == 0:
        words +='buzz'
    if not words:
        return x
    return words
