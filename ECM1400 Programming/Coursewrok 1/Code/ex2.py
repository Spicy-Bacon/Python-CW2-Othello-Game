def email_addresses(first, last, domain = '@exeter.ac.uk'): #returning the default domain as @exeter.ac.uk
    emails = [] #creat empty list
    for i in range(min(len(first), len(last))): #name must have both fist and last name to be taken into the loop. 
        first_name = first[i] 
        last_name = last[i] 
        email = (f'{first_name[0].lower()}.{last_name.lower()}{domain}') 
        emails.append(email) #add the result to the list

    return emails #the function will return the emails list 












   
    




