base = {
    0: "",
    1: "0",
    2: "00",
    3: "000",
    4: "01",
    5: "1",
    6: "10",
    7: "100",
    8: "1000",
    9: "02"}

rom = [ "I", "V", "X", "L", "C", "D", "M" ]

def roman(number):
    numstr = str(number)
    return "".join(part for part in ["".join(rom[int(i) + 2 * n] for i in base[int(numstr[-1 - n])]) for n in range(len(numstr))][::-1])
