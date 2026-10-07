def palindrome_detector(phrase):
    phrase = phrase.lower() #convert the snetance to lower caase
    sentence = '' #create an empty string to later add the characters
    for character in phrase:
        if character.isalnum(): #check if the the character is a letter
            sentence += character #add the character to the empty string if it is a letter
    
    return sentence == sentence[::-1] #compare the santance with a reversed version and return a boolean value to the
