def is_valid(isbn):
    isbn = isbn.replace('-', '')
    summation = 0
    if len(isbn) is not 10:
        return False
    for i in range(10):
        if isbn[i] == 'X' and i == 9:
            summation += 10
        elif isbn[i].isdigit():
            summation += int(isbn[i])*(10-i)
        else:
            return False
    return summation % 11 == 0