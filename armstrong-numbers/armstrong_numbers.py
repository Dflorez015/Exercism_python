def is_armstrong_number(number):
    numberstr = [int(x) for x in str(number)]
    size = len(numberstr)
    suma = 0
    for x in numberstr:
        suma += x**size
    return number == suma   

