
def abbreviate(words):
  words = words.replace("_","")    
  words = words.replace("-"," ")
  words = words.replace(",","")
  words = words.replace("'","")
  print(words)
  acronym = ''.join(word[0] for word in words.upper().split())
  return acronym
