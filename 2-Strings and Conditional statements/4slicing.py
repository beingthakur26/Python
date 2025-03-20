#Slicing
#Slicing is used to extract a part of a string. The syntax for slicing is [start:stop]. The start index is included and the stop index is excluded. If the start index is not specified, the slice starts from the beginning of the string. If the stop index is not specified, the slice goes to the end of the string.
#Example :

str = "Manas Singh"
print(str[1:4]) # ana
print(str[6:11]) # Singh
print(str[6:len(str)]) # Singh
print(str[6:]) # Singh
print(str[:5]) # Manas

#slicing
#Negative indexing
#Negative indexing is used to access the characters from the end of the string. The index of the last character is -1, the second last character is -2, and so on.
#Example :

str = "Manas"
print(str[-5:-1]) # Mana
print(str[-5:]) # Manas
print(str[:-1]) # Mana  (last character is not included)
print(str[-1:]) # s
print(str[-1]) # s
print(str[-2]) # a