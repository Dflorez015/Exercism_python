def color_bands(color):
    bands = {     
            "black": "0",
            "brown": "1",
            "red": "2",
            "orange": "3",
            "yellow": "4",
            "green": "5",
            "blue": "6",
            "violet": "7",
            "grey": "8",
            "white": "9"
            }
    return bands[color]

def value(colors):
    return int(color_bands(colors[0]) + color_bands(colors[1]))
