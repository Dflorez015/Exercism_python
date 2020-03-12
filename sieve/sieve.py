def primes(limit):
    if limit == 1:
        return []
    values = list(range(2, limit + 1))
    for n in range(2, limit + 1):
        for m in range(2, limit + 1):
            if n*m in values:
                values.remove(n * m)
    return values