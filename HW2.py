def reverse(sentence, reverse_word):
    if ((type(sentence)!= str) or (type(reverse_word)!= str)) :
        return("invalid input")
    if reverse_word not in sentence:
        return ("The word was not found")
    return(sentence.replace(reverse_word, reverse_word[::-1],1))
  
        
        


