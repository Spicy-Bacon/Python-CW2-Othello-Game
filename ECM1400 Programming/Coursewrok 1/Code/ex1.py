def kelvin(temperature, to_kelvin=True): #set default return value of to_kelvin to true
    if to_kelvin: 
        converted = temperature + 273.3 #celsius to kelvin
    else:
        converted = temperature - 273.3 #kelvin to celsius
    return round(converted) #round of the converted temperature to nearest integer