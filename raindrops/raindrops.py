def convert(number):

    def has_factor(number, factor):
        return number % factor == 0

    conversion_dict = {3:"Pling", 5:"Plang", 7:"Plong"}
    result = ""
    for factor in sorted(conversion_dict):
        if has_factor(number, factor):
            result = result + conversion_dict.get(factor)
    if result == "":
        return str(number)
    return result
