def steps(number):
    cont = 0
    if number <= 0:
        raise ValueError('Solo números postitivos')
    while number != 1 : 
        cont += 1
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
    return cont

