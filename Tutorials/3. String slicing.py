# -variabel[] funktion-
namn = "Alexander Olivius"
first = namn[0:9] #Här är steg by default 1 och blir bara "Alexander"
last = namn[10:17:2] # namn[start:stop:steg] i det här fallet tas varannan bokstav och blir Oiis
print("Hej " + namn + " från din input är ditt efternamn " + last + " och förnamn " + first + ".")
#Om start och stop i namn[start:stop:steg] lämnas tom så räknar python start som 0 och stop som allra sista bokstaven

back_o_fram = namn[::-1] #om steg är -1 blir variabeln namn back och fram
print(back_o_fram)

# -slice() funktion-
website1 = "http://google.com"
website2 = "http://wikipedia.com"

slicee = slice(7,-4) 
#Slice funktion använder sig också av start, stop och steg-
#-fast med komma tecken istället för kolon emellan
#Dock börjar stop delen från slutet av var med varje index som + (-1)
#Med -4 tar vi bort ".com" från varje webside namn där "m" har index -1 och "." har -4 
print(website1[slicee])
print(website2[slicee])
