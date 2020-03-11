def triplets_with_sum(number):
    return  triplets_in_range(1, number)


def triplets_in_range(start, end):
    triplets = []
    for a in range(start, (end+2) // 2):
        aux = end - a
        for b in range(a+1, (aux+2) // 2):
            c = aux - b
            if is_triplet([a, b, c]):
                triplets.append([a, b, c])
    return triplets


def is_triplet(triplet):
    c = triplet[0]**2 + triplet[1]**2
    return c == triplet[2]**2
      