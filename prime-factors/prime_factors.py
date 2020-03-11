def factors(value):
    x = 2
    num_p = []
    while value != 1:
        if value % x == 0:
            value /= x
            num_p.append(x)
        else:
            x += 1
    return num_p
