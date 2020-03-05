
def count_words(sentence):    
    signs = "123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ' "
    for x in sentence:
        if signs.count(x) == 0:         
            sentence = sentence.replace(x," ")
        elif sentence.count("don't") <= 1:
            if sentence.count("'") > 1:               
                    sentence = sentence.replace("'"," ")      
    sentence = sentence.replace("can t", "can't")
    words = list(sentence.casefold().split())
    return {x: words.count(x) for x in words}

