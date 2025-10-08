# -Multiple Assignment-

namn = "Alex"
ålder = 17 
höjd = 173.5
snygghet = True 

namn, ålder, höjd, snygghet = "Alex", 17, 173.5, True #En linje av kod istället för 4 ovanför

print("Namn: " + str(namn))
print("Ålder: " + str(ålder) + " år")
print("Höjd: " + str(höjd) + "cm")
print("Är subjektet snygg?: " + str(snygghet))

Alex = 30
Anja = 30
Anton = 30
Adam = 30

Alex = Anja = Anton = Adam = 30 #Variabler med lika integer data-typ kan skrivas såhära

print(Alex)
print(Anja)
print(Anton)
print(Adam)

# -Olika string methods-

name = "Alex Oliv "

print(len(name))
print(name.find("A")) #Hittar index för bokstäver
print(name.upper()) #Allt i upper case
print(name.title()) #Första bokstav i alla ord i upper case
print(name.capitalize()) #Första bokstav i upper case
print(name.lower()) #Allt är i lower case
print(name.isdigit()) #Visar True eller False om stringen är ett "nummer"
print(name.isalpha()) #Visar True eller False beroende på om det är alfabetiskt eller inte
print(name.count("l")) #Ger värde på antal bokstäver inom ()
print(name.replace("Alex", "Bertil")) #kan byta ut ord
#eller
print(name.replace("l", "r")) #kan byta ut bokstäver
print(name*20) #multiplicerar variablen x gånger


# -String Formating- or str.format() = optional method that gives users more control when displaying output 
animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item) #istället för att skriva detta kan det skrivas som nedan, på ett mer elegant sätt
print("The {} jumped over the {}".format(animal, item)) #där variabler kan implementeras markeras med en format field "{}", inom .format() kan de variabler som vill has i print() skrivas
print("The {} jumped over the {}".format(item, animal)) #det kan också skrivas tvärtom och då skrivs det annorlunda
print("The {0} jumped over the {1}".format(item, animal)) #man kan också skriva indexen till variablerna som korresponderar till .format()
print("The {animal} jumped over the {animal}".format(item = "moon", animal = "cow")) #kan också använda sig av "keyword arguments", här skrivs "cow" två ggr
text = "The {} jumped over the {}"
print(text.format(animal, item)) #detta funkar också och printar exakt samma sak

name = "Alex"
print("Hello my name is {}".format(name)) #vanlig string format
print("Hello my name is {name:10}".format(name)) #string formatting där name variabeln är efterföljd av 10 mellansteg, kallas left align
print("Hello my name is {:<10}".format(name)) #det här är också left align för att variabeln kommer visas innan 10 mellansteg
print("Hello my name is {:>10}".format(name)) #det här är right align för att variebeln kommer visas efter eller större än 10 mellansteg 
print("Hello my name is {:^10}".format(name)) #det här är center align, alltså att variabeln visas i centret av 10 mellansteg, liknas vid .center(10) string metoden

number = 100000
print("The number is {:.3f}".format(number)) #skriver numret med 3 decimaler och avrundar, .xf där f står för floating point
print("The number is {:,}".format(number)) #skriver numret med komma tecken emellan varje tre nummer som tex 1,000
print("The number is {:b}".format(number)) #skriver numret i binärt
print("The number is {:o}".format(number)) #skriver det i oktalt
print("The number is {:X}".format(number)) #skriver det i hexadecimal
print("The number is {:E}".format(number)) #skriver det i vetenskaplig format som tex 1,00000E+03 alltså 1000



# -Type casting-

x = 5 #int
y = 2.0 #float
z = "6" #str

x = str(x) #typecastar integer av 5 till en string
y = int(y) #typecastar en float av 2.0 till en integer av 2
z = float(z) #typecastar en string av "6" till en float av 6.0
 
print("Hej din jävla " + x + "-åring.")
print(y)
print(z*3)

# -Math Functions-
import math 
# + för addition
# - för substraktion
# / för division
# * för multiplikation
# % för kvarvarande divisioner inom en division/bråk, tex 5/3 har en kvarvarande av 2

#Exempel för %
x = int(input("What's x?: "))
if x % 2 == 0: #tex 5/2 är detsamma som 2 + (1/2). Därför är det != 0 eftersom 1/2 är inte 0
    print("Even")
else:
    print("Odd")


pi = -3.14 
print(round(pi,2)) #avrundar til två decimal
print(abs(pi)) #absoluta värdet för ett number 
print(math.floor(pi)) #min värdet för ett nummer 
print(math.ceil(pi)) #max värdet för ett nummer 
print(pi**2) #upphöjt i två 
print(math.pow(pi, 2)) #upphöjt i två, bara ett annat sätt att skriva
print(math.sqrt(420)) #roten ur 420

x = 510
y = 352
z = 896
w = 648
print(max(x, y, z, w)) #tar fram det största värdet
print(min(x, y, z, w)) #tar fram det minsta värdet 

print(f"{1000:,}") #printar 1000 som 1,000 mha f-strings och kolon som specifierar kommat
print(f"{0.656123:.2f}") #printar bara två decimaler, ett annat sätt att avrunda fast utan round() funktionen

#----------------------------------------------------------------------------------------------------------------
#Walruss Operator := - assigns values to variables as part of a larger expresssion (aka assignment expression)
#----------------------------------------------------------------------------------------------------------------

food = list()
while True:
    foods = input("Vad är din favo mat?: ")
    if foods == "quit":
        break
    food.append(foods)

#med := kan algo'n skrivas så här (mycket kortare)

food = list()
while foods := input("Vad är din favo mat?: ") != "quit":
    food.append(foods)

#sådär mycket bättre 

#----------------------------------------------------------------------------------------------------------------
#assigning functions to variables, aka assigning aliases to functions
#----------------------------------------------------------------------------------------------------------------

def hello():
    print("Hi hello what's upp")

hi = hello 
hi() #vi har get def hello() ett alias genom linje 150 som är hi()

#----

p = print
p("Hej") #vi har gett print funktionen ett alias a p 