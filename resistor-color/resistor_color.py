def color_bands(color):
    bands = {     
            "black": 0,
            "brown": 1,
            "red": 2,
            "orange": 3,
            "yellow": 4,
            "green": 5,
            "blue": 6,
            "violet": 7,
            "grey": 8,
            "white": 9
            }
    if color.isdigit():
        return bands[color]
    else:
        return bands[color]

def color_code(color):
    return color_bands(color)

def colors():
  return [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
