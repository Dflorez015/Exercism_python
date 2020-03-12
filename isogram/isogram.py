def is_isogram(string):
    string = string.lower().replace(" ","")
    string = string.replace("-","")
    for ch in string:        
        if string.count(ch) > 1:
            return False
    return True    
        
