# list = en ensam variabel som lagrar flera objekt inom sig

låda = ["Tejp","Hammare","Skruvmejsel","Skiftnyckel"]

låda[0] = "Silvertejp" #man kan ändra lista närsomhelst mha denna kod

valt = int(input("Random sak från lådan, välj nummer från 1-4: ")) 
Riktig_Valt = valt - 1
print(låda[Riktig_Valt])
#ovan är det ett litet system som outputtar obejktet baserat på respektive inskrivet index

#Olika funktioner för listor
låda.append("Blöt strumpa") #lägger till ett objekt på slutet av listan
låda.remove("Skiftnyckel") #tar bort ett specifierat objekt från listan 
låda.pop() #tar bort det sista objektet på listan
låda.insert(2,"Kaka") #Tillfogar ett objekt på specifierat index och flyttar upp alla efter
låda.sort() #sorterar alfabetisk ordning
låda.clear() #tar bort allt från listan

for i in låda: #simpel for loop som skriver ut alla objekt i listan 
    print(i)

#2d lists = en lista för flera listor
drinks = ["Coca-Cola","Vatten","Mjölk"] #Individuella listor i.e. vanliga lists
middag = ["Fisk","Kött","Kyckling"]
desert = ["Glass","Kaka","Godis"]

mat = [drinks,middag,desert] #multidimensionella lista

print(mat[1][0]) #printar de specifierade index deriktorierna, i.e. middag-> fisk






#Tuple = en samling som är ordnad och inte kan förändras, 
#        används för att gruppera relaterad data

student = ("Alex",17,"male") #istället för rektangel parenteser som i lists så är det vanliga
print(student.count("Alex")) #visar antalet ggr Alex visas i tuplen 
print(student.index("male")) #visar index för ordet male i tuplen

for i in student: #simpel for loop som skriver ut alla objekt i tuplen
    print(i)

if "Alex" in student: #if statement som visar om Alex finns i tuplen
    print("Alex är här")





# Set = en samling som är oordnad, inte har index eller dubbla valörer

bestik = {"Gaffel","Kniv","Sked","Sked","Sked","Sked","Sked"} 
porslin = {"Talrik","Tefat","Skål","Djuptalrik","Sked"}
# Jämfört med listor skrivs sets med curly braces istället

#Olika funktioner för sets
bestik.add("Servett") #lägger till "Servett" till settet
bestik.remove("Kniv") #tar bort "kniv" från settet
bestik.clear() #tar bort allt
bestik.update(porslin) #lägger till settet porslin in till settet bestik, vice versa
middagsbord = porslin.union(bestik) #lägger båda sättet i ett nytt set, går vice versa

print(bestik.difference(porslin)) #liknelser i settens innehåll, går också vice versa
print(porslin.intersection(bestik)) #skillnader i settens innehåll, går också vice versa

for i in bestik:
    print(i) #detta kommer printa bestiken i en oordnad lista och ignorera alla dubbla "sked"






# dictionary = En föränderlig, oordnad samling av unika nyckel:värde par
#             Snabbt för att det använder hashing, tillåter oss att nå värden snabbt
capitals = {
    "USA":"Washington DC",
    "India":"New Delhi",
    "China":"Beijing",
    "Russia":"Moscow"
}

capitals.update({"Germany":"Berlin"}) #lägger till ett par till dictionarien
capitals.update({"USA":"Las Vegas"}) #updaterar values hos keys i dictionarien
capitals.pop({"China"}) #tar bort specifierad key och dess value
capitals.clear() #tar bort allt

print(capitals["Germany"]) #Detta kommer ge en error därför bättre att använda koden nedan
print(capitals.get("Germany")) #Detta ger en output av None istället för en error, alltså säkrare
print(capitals.keys()) #printar bara nyckelorden, i det här fallet länderna
print(capitals.values()) #printar bara valörerna hos nyckelorden, i.e. huvudstäderna
print(capitals.items()) #printar allting

for key,value in capitals:
    print(key,value) #for loop som printar också allting

#annat exempel av dictionaries
students = {
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin",
}

for student in students:
    print(student,students[student], sep=", ") #printar alla keys och dess values 





#kombinera lists o dictionaries - man vet att det är en list pga square brackets,
#men varje objekt i listan är en dictionary i sig självt!
students = [
    {"name":"Hermione", "house":"Gryffindor", "petronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "petronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "petronus":"Jack Russel"},
    {"name":"Draco", "house":"Slytherin", "petronus":None} #None i python specifierar Inget
]
for student in students:
    print(student["name"], student["house"], student["petronus"], sep=", ") 
#ovan printas allt i listans dictionaries med komma tecken imellan varje ny value!





#Match = matchar en input med redan definierade variabler-ish
name = input("What is your name?: ")

match name:
    case "Harry" | "Hermione" | "Ron": #| markerar ett nytt case men som printar samma sak
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?") #printar "Who?" för alla odefinierade "cases", markeras med _