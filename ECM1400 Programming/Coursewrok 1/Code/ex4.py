def obfuscate(text):
    starting_space = text.startswith(' ') #check if there is a space in the start of the original sentence
    ending_space = text.endswith(' ') #check if there is a space in the start of the original sentence

    splitted = text.strip().split(' ')  #remove the spaces and crearte a list of words
    sentence = []

    for word in splitted: #check every word in the list
        if word.lower() == 'the': 
            sentence.append('and') #if the item in the list is 'the', change it to 'and'
        elif word.lower() == 'and':
            sentence.append('the') #if the item in the list is 'and', change it to 'the'
        else:
            sentence.append(word) #the the item in the list is neither 'the' or 'and', append the word to the empty list
    
    text = ' '.join(sentence) #join every word toghtger with a space

    character = list(text) #split the text into list of characters 
    for i in range(2, len(character), 3): #start with the third character to the length of the total number of characters in a step of 3
        character[i] = character[i].upper() #convert the character in the range and convert them to upper case
    
    text = ''.join(character) #join the characters back to a complete text without space in between, because there is ' ' already in the original list
    
    splitted = text.split(' ') #split the sentence into list of words again
    for i in range(4, len(splitted), 5): #start with the fifth word to the length of the total number of words in a step of 5
        splitted[i] = splitted[i][::-1] #reverse the word in the range

    smallcaps = list('abcdefghijklmnopqrstuvwxyz') #make a list of small caps and big caps alphabets
    caps = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    for i in range(1, len(splitted), 2): #for every other words
        word = splitted[i] #split the word into list of letters
        new_word = '' 

        for ch in word: 
            if ch in smallcaps: #converting small caps into caps
                index = smallcaps.index(ch) #fing the letter's index in the small caps list
                new_word += smallcaps[(index + 1) % 26] #convert the letter with key 1, and if the letter is 'z' it will be converted to 'a'
            elif ch in caps: #converting caps into small caps
                index = caps.index(ch) #fing the letter's index in the caps list
                new_word += caps[(index + 1) % 26] #convert the letter with key 1, and if the letter is 'Z' it will be converted to 'A'
            else:
                new_word += ch  # keep non-letters
        splitted[i] = new_word #update the word in the list

    text = ' '.join(splitted) #join the list of words back together with a space

    if starting_space: #put the starting space back, if removed at the start of the function
        text = ' ' + text
    if ending_space: #put the ending space back, if removed at the start of the function
        text = text + ' '

    return text #return the value to the function