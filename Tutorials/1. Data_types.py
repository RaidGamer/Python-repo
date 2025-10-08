import math #imports should always be on top

# String data type  

#-fstrings- or format strings
name = "Alexander Olivius"
print(f"Hej jag heter {name}!")

# -literal assignment- 
first = "Alexander" #can be written with str() but essentially they're the same thing without
last = str("Olivius") 

# -constructor function- (Checks type of variable)
print(type(first)) #shows the type of variable, in this case string
print(type(first) == str) #Checks if var type is equal to a string, in this case true
print(isinstance(first, str)) #checks if the instance of var first is a string, which is true

# -Concatenation-
fullname = first + " " + last #adds var first and last together to a unified var
print(fullname)

fullname += "!" #adds a exclamation mark to the var
print(fullname)

# -Casting a number to a string-
goodOldays1 = str(2006) #converts the integer of 2006 to a string
print(type(goodOldays1)) #shows that 2006 is now a string
print(goodOldays1)

goodOldays2 = 2006 #stays a integer
print(type(goodOldays2)) #shows that 2006 is still a integer
print(goodOldays2)

statement = "Back in " + goodOldays1 + " I was an unborn baby yet to come out of the cave." #concatenation with var and strings
print(statement)

# -Multiple lines-
multiline = ''' 
Hello, I'm froggy doe. 

Your personal assistant!
                                Kys.

''' #vars can be written free-form with tripple ''' '''
print(multiline)

# -Escaping special characters- i.e. escape sequences 
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?' # (\') (\t) (\n) (\\)
print(sentence)

# -String Methods- 

print(first)
print(first.lower()) #brings everything to lower case
print(first.upper()) #brings everything to upper case
print(first)

print(multiline.title()) #capitalises first letter in every word
print(multiline.replace("personal" , "public")) #replaces string of letters with another
print(multiline)

print(len(multiline)) #counts number of characters in variable
multiline += "                               "
multiline = "                         " + multiline 
print(len(multiline))

print(len(multiline.strip())) #shows the length of multiline when stripped
print(len(multiline.lstrip())) #shows the length of multiline, left, when stripped
print(len(multiline.rstrip())) #shows the length of multiline, right, when stripped

print(" ")

# -Build a menu-
title = "menu".upper() 
print(title.center(20, "=")) 
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
print("="*20)

# -String index values- almost like string slicing
print(first[1]) #provides second letter in my name, 0 is the first
print(first[-1]) #provides last letter in my name
print(first[1:-1]) #provides first letter until last letter (excluding last)
print(first[1:]) #provides second to last letter of my name
print(first[0:]) #provides first to last letter of my name

# -Some methods return boolean data-
print(first.startswith("A")) #output is true because var first starts with A
print(first.endswith("r")) #output is true because var first ends with r, not R

# -Boolean data type- (is True or False)
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# -Numeric data types-

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# -float type- (ability to include decimals)
gpa = 3.28 
y = float(1.14)
print(type(gpa))

# -complex type- (komplexa tal)
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# -Built in functions for numbers-

print(abs(gpa)) #absolute value (abs)
print(abs(gpa * -1)) #still returns 3,28 because it only cares for values not minus or plus

print(round(gpa)) #rounds up (round)

print(round(gpa, 1)) #rounds to one decimal

print(math.pi)
print(math.sqrt(64)) #square root of 64 is 8
print(math.ceil(gpa)) #the max number of 3,28 is 4
print(math.floor(gpa)) #the minimum number of 3,28 is 3

# -Casting a string to a number-
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# -Error if you attempt to cast incorrect data-
zip_value = int("New York") #doesn't work because words are not values, therefore not integers