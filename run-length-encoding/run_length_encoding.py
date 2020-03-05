from itertools import groupby

def decode(string):
    result = []
    count = 0
    for char in string:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            result.append(char * max(1, count))
            count = 0
    return "".join(result)

def encode(string):
    result = []
    for char, group in groupby(string):
        count = sum(1 for _ in group)
        if count > 1:
            result.append(str(count))
        result.append(char)
    return "".join(result)