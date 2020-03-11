def distance(strand_a, strand_b):
    a = len(strand_a)
    b = len(strand_b)
    if a != b:
        raise ValueError("Error: Los parámetros no tienen el mismo tamaño.")
    distance = 0
    for d in range(a):
        if strand_a[d] != strand_b[d]:
            distance += 1
    return distance