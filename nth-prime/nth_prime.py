def prime(number):
    if number < 1:
        raise ValueError ("Número menor a 1")
    n = 2
    primes = []
    while (True):
        for p in primes: 
            if n % p == 0:
                n += 1
                break
        else:
            primes.append(n)
            if len(primes) == number:
                return (n)
