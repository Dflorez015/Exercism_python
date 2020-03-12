def is_pangram(sentence):
    letters = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    for vo in letters:
        if sentence.count(vo) < 1:
            return False
    return True   
