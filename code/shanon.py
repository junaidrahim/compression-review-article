def float_bin(number, places = 6): 
    whole, dec = str(number).split(".") 

    whole = int(whole) 
    dec = int (dec) 
  
    res = bin(whole).lstrip("0b") + "."

    for x in range(places): 
        whole, dec = str((decimal_converter(dec)) * 2).split(".") 
        dec = int(dec) 
        res += whole   
    return res 
  
def decimal_converter(num):  
    while num > 1: 
        num /= 10
    return num 


d = list("lossless data compression")
unique_alphabets = set(d)

probabilities = {}

for i in unique_alphabets:
    probabilities[i] = 0

for i in unique_alphabets:
    probabilities[i] = d.count(i) / len(d)

sorted_probabilities = {letter: prob for letter,prob in sorted(probabilities.items(), key=lambda item: item[1])}
print(sorted_probabilities)