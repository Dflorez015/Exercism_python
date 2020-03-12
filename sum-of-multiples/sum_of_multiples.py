def sum_of_multiples(limit, multiples):
    return sum({num for m in multiples 
                if m != 0
                for num in range(0, limit, m)})