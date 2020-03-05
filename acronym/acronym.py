
def abbreviate(words):
  words = words.replace("_","")    
  words = words.replace("-"," ")
  words = words.replace(",","")
  words = words.replace("'","")
  acronym = ''.join(word[0] for word in words.upper().split())
  return acronym
